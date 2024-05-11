import logging

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .celery.celery_app import app as celery_app
from .checks import check_redis_connection, check_s3_connection, upload_string_to_s3

app = FastAPI()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Assuming you have a similar check_s3_connection function as before
    s3_status = "online" if await check_s3_connection() else "offline"
    redis_status = "online" if await check_redis_connection() else "offline"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "s3_status": s3_status, "redis_status": redis_status},
    )


@app.get("/upload", response_class=HTMLResponse)
async def upload_test_file(request: Request):
    bucket_name = "test"
    filename = await upload_string_to_s3(bucket_name)
    task = celery_app.send_task(
        "test_task",
        args=[
            bucket_name,
            filename,
        ],
    )

    url = app.url_path_for("get_result", task_id=task.id)

    return RedirectResponse(url=url)


@app.get("/get-result/{task_id}", name="get_result")
async def get_result(request: Request, task_id: str):
    task = celery_app.AsyncResult(task_id)
    context = {"request": request, "status": task.state, "result": None, "reason": None}
    if task.state == "SUCCESS":
        context["result"] = task.result
    elif task.state == "FAILURE":
        context["reason"] = str(task.result)
    return templates.TemplateResponse("result.html", context)

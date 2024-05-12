import logging

from .celery.celery_app import app as celery_app
from .s3 import global_s3_client

logger = logging.getLogger(__name__)


@celery_app.task(name="test_task")
def test_task(bucket_name: str, filename: str):
    logger.info(f"Got Task to donload file: {filename} from bucket {bucket_name}")

    response = global_s3_client.get_object(Bucket=bucket_name, Key=filename)
    content = response["Body"].read().decode("utf-8")

    logger.info(f"File content: {content}")

    return content

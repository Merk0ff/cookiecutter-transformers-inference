# Broker settings.
broker_url = "{{ cookiecutter.redis_url }}"


# Using the database to store task state and results.
result_backend = "{{ cookiecutter.redis_url }}"

task_annotations = {"*": {"rate_limit": "10/s"}}

# task_queues = {
#     "ml-queue": {
#         "exchange": "ml-queue",
#     }
# }
# task_routes = {"worker.celery_worker.long_task": "ml-queue"}

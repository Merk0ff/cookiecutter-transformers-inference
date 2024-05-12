from apps.settings import global_settings

# Broker settings.
broker_url = global_settings.redis_url

# List of modules to import when the Celery worker starts.
imports = ("apps.tasks",)

# Using the database to store task state and results.
result_backend = global_settings.redis_url

task_annotations = {"*": {"rate_limit": "10/s"}}

task_track_started = True

worker_concurrency = 1
worker_prefetch_multiplier = 1

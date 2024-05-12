from apps.settings import global_settings

# Broker settings.
broker_url = global_settings.redis_url


# Using the database to store task state and results.
result_backend = global_settings.redis_url

task_annotations = {"*": {"rate_limit": "10/s"}}

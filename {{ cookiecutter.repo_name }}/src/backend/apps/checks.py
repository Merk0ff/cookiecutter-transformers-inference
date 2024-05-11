from io import StringIO
from uuid import uuid4

import redis.asyncio as redis
from botocore.exceptions import EndpointConnectionError, NoCredentialsError

from .s3 import global_s3_session

redis_client = redis.from_url("{{ cookiecutter.redis_url }}", decode_responses=True)


async def check_s3_connection():
    try:
        async with global_s3_session as s3_client:
            await s3_client.list_buckets()
        return True
    except (EndpointConnectionError, NoCredentialsError):
        return False


async def check_redis_connection():
    try:
        # Use the asynchronous Redis PING command
        response = await redis_client.ping()
        return response
    except redis.exceptions.ConnectionError:
        return False


async def upload_string_to_s3(bucket_name="test") -> str:
    file_like_object = StringIO("Test data")

    # Use aioboto3 to upload the file-like object
    async with global_s3_session as s3_client:
        filename = f"{uuid4()}.txt"

        await s3_client.put_object(
            Bucket=bucket_name, Key=filename, Body=file_like_object.getvalue()
        )

    return filename

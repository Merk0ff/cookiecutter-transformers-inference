from io import StringIO
from uuid import uuid4

import aioboto3
import redis.asyncio as redis
from botocore.config import Config
from botocore.exceptions import EndpointConnectionError, NoCredentialsError

redis_client = redis.from_url("{{ cookiecutter.redis_url }}", decode_responses=True)


async def check_s3_connection():
    try:
        async with aioboto3.Session().client(
            "s3",
            endpoint_url="{{ cookiecutter.s3_endpoint }}",
            aws_access_key_id="{{ cookiecutter.minio_root_user }}",
            aws_secret_access_key="{{ cookiecutter.minio_root_password }}",
            aws_session_token=None,
            config=Config(signature_version="s3v4"),
            verify=False,
        ) as s3_client:
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
    async with aioboto3.Session().client(
        "s3",
        endpoint_url="{{ cookiecutter.s3_endpoint }}",
        aws_access_key_id="{{ cookiecutter.minio_root_user }}",
        aws_secret_access_key="{{ cookiecutter.minio_root_password }}",
        config=Config(signature_version="s3v4"),
        verify=False,
    ) as s3_client:
        filename = f"{uuid4()}.txt"

        await s3_client.put_object(
            Bucket=bucket_name, Key=filename, Body=file_like_object.getvalue()
        )

    return filename

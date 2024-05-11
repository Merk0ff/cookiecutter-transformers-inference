import logging

import boto3
from botocore.config import Config

from .celery.celery_app import app as celery_app

logger = logging.getLogger(__name__)
s3 = boto3.client(
    "s3",
    endpoint_url="{{ cookiecutter.s3_endpoint }}",
    aws_access_key_id="{{ cookiecutter.minio_root_user }}",
    aws_secret_access_key="{{ cookiecutter.minio_root_password }}",
    aws_session_token=None,
    config=Config(signature_version="s3v4"),
    verify=False,
)


@celery_app.task(name="test_task")
def test_task(bucket_name: str, filename: str):
    logger.info(f"Got Task to donload file: {filename} from bucket {bucket_name}")

    response = s3.get_object(Bucket=bucket_name, Key=filename)
    content = response["Body"].read().decode("utf-8")

    logger.info(f"File content: {content}")

    return content

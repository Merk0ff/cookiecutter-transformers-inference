import boto3
from botocore.config import Config

from .settings import global_settings

global_s3_client = boto3.client(
    "s3",
    endpoint_url=global_settings.s3_url,
    aws_access_key_id=global_settings.s3_access_key,
    aws_secret_access_key=global_settings.s3_secret_key,
    aws_session_token=None,
    config=Config(signature_version="s3v4"),
    verify=False,
)

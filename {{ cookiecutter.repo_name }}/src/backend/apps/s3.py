import aioboto3
from botocore.config import Config


class S3Manager:
    def __init__(
        self,
        endpoint_url: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
    ):
        self.endpoint_url = endpoint_url
        self.session = aioboto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=None,
        )

    async def __aenter__(self):
        async with self.session.client(
            service_name="s3",
            endpoint_url=self.endpoint_url,
            config=Config(signature_version="s3v4"),
            verify=False,
        ) as client:
            self.s3_client = client
            return client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.s3_client:
            await self.s3_client.close()


global_s3_session = S3Manager(
    endpoint_url="{{ cookiecutter.s3_endpoint }}",
    aws_access_key_id="{{ cookiecutter.minio_root_user }}",
    aws_secret_access_key="{{ cookiecutter.minio_root_password }}",
)

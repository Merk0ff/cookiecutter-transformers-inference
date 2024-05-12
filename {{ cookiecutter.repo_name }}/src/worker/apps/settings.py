from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_url: str
    s3_url: str
    s3_access_key: str
    s3_secret_key: str


global_settings = Settings()

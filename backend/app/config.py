from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "short-url"
    BASE_URL: str = "http://127.0.0.1:80"

    MONGO_HOST: SecretStr
    MONGO_DB: SecretStr
    MONGO_PORT: SecretStr
    MONGO_USER: SecretStr
    MONGO_PASSWORD: SecretStr

    class Congig:
        env_file = ".env.dev"


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file: str = ".env"


settings: Settings = Settings()    # pyright: ignore[reportCallIssue]

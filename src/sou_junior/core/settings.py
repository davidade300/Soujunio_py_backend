import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    base class for application settings
    """

    DATABASE_URL: str = str(os.getenv("DATABASE_URL"))


settings: Settings = Settings()  # pyright: ignore[reportCallIssue]

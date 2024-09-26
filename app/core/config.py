from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent
ENV_FILE_PATH = BASE_DIR / ".env"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    host: str = Field(..., alias="DB_HOST")
    port: int = Field(..., alias="DB_PORT")
    user: str = Field(..., alias="DB_USER")
    name: str = Field(..., alias="DB_NAME")
    password: str = Field(..., alias="DB_PASSWORD")
    echo: bool = Field(default=False, alias="DB_ECHO")


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()


def get_db_url() -> str:
    return (
        f"postgresql+asyncpg://{settings.db.user}:{settings.db.password}@"
        f"{settings.db.host}:{settings.db.port}/{settings.db.name}"
    )


if __name__ == "__main__":
    print(settings.model_dump())
    print(get_db_url())

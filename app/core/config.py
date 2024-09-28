from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent
ENV_FILE_PATH = BASE_DIR / ".env"


class DatabaseSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = "5432"
    user: str = "user"
    name: str = "name_database"
    password: str = "password"
    echo: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding="utf-8",
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )
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

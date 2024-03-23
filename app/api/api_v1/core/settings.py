from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    env_path: str = str(Path(__file__).resolve().absolute().parents[3] / ".env-dev")
    model_config = SettingsConfigDict(env_file=env_path)
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def mongodb_conn_string(self) -> str:
        return f"mongodb://{self.DB_HOST}:{self.DB_PORT}/"


settings = Settings()

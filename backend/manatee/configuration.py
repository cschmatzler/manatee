import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str

    API_HOST: str
    API_PORT: str

    DATABASE_PROVIDER: str


class DevelopmentSettings(Settings):
    DATABASE_FILENAME: str

    class Config:
        env_file = "development.env"


class ProductionSettings(Settings):
    DATABASE_SOCKET: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str

    class Config:
        env_file = "production.env"


class SettingsFactory:
    def __init__(self):
        self.env = os.environ.get("MANATEE_ENV", "development")

    def __call__(self):
        if self.env == "production":
            return ProductionSettings()
        else:
            return DevelopmentSettings()


settings = SettingsFactory()()

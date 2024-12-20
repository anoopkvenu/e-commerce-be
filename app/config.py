import os
from sqlalchemy.engine import URL


class Settings:
    PROJECT_NAME = "E Commerce Site"
    PROJECT_VERSION = "1"
    DATABASE_URL = {
        "drivername": "postgresql",
        "username": os.getenv("DB_USER_NAME", "be_service"),
        "password": os.getenv("DB_PASSWORD", "qwerty@123"),
        "host": os.getenv("DB_HOST", "db"),
        "database": os.getenv("DB_NAME", "e_commerce_db"),
        "port": os.getenv("DB_PORT", 5432)
    }
    TEST_DATABASE = {
        "drivername": "postgresql",
        "username": os.getenv("DB_USER_NAME", "be_service"),
        "password": os.getenv("DB_PASSWORD", "qwerty@123"),
        "host": os.getenv("DB_HOST", "db"),
        "database": os.getenv("DB_NAME", "TEST"),
        "port": os.getenv("DB_PORT", 5432)
    }
    TEST_DATABASE_URL = URL.create(
        **TEST_DATABASE
    )

settings = Settings()
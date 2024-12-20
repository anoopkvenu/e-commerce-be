import os


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

settings = Settings()
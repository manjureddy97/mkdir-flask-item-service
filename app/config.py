import os


class Config:
    # SQLite DB in project root by default
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///items.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True

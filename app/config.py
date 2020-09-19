import os
from os import environ

APP_NAME = 'app'  # ! rename app :)
ENV = environ.get(F'{APP_NAME}_ENV', 'prod')  # when testing set {APP_NAME}_ENV=test
DB_URI = os.environ.get(f'{APP_NAME}_DB_URI', f"postgresql://postgres:postgres@db:5432/{APP_NAME}_db")

HOUR = (60 * 60)
DAY = (HOUR * 24)


class Config:
    SECRET_KEY = 'top-secret'  # ! always read secret from env var
    JWT_ACCESS_TOKEN_EXPIRES = (1 * DAY)  # ! always set reasonable value ;)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TConfig:
    SECRET_KEY = "not-so-secret"
    JWT_ACCESS_TOKEN_EXPIRES = False

    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:postgres@localhost:5432/{APP_NAME}_db_test"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

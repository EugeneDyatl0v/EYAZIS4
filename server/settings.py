import os

LOGGER_PREFIX = 'translator.'


class Database:
    prefix = 'translator_'
    url = os.getenv('DATABASE_URL')

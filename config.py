import os
from re import DEBUG

class Config:
    SECRET_KEY = 'YOUcantHackThis'


class ProdConfig(Config):
      SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:malika@localhost/pitch'
class DevConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:malika@localhost/pitch'
      DEBUG = True

config_options = {
     'development': DevConfig,
     'production': ProdConfig,
     'test': TestConfig
}


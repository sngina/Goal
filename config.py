import os

class Config:
    SECRET_KEY = os.environ.get('YOUcantHackThis')


class ProdConfig(Config):
      SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:malika@localhost/pitch'
class DevConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:malika@localhost/pitch'


config_options = {
     'development': DevConfig,
     'production': ProdConfig,
     'test': TestConfig
}


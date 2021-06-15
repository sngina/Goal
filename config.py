import os


class Config:
    SECRET_KEY = 'YOUcantHackThis'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:malika@localhost/one_minute_pitch'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("stella.kimaru@student.moringaschool.com")
    MAIL_PASSWORD = os.environ.get("kimaru@2015!")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

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

import os
class Config:
    '''configuration for the parent class'''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'

    # @staticmethod
    # def init_app(app):
    #     pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'
    # pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'tests':TestConfig
}
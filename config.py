import os
class Config:
    '''configuration for the parent class'''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '10silvianjoki@gmail.com'
    MAIL_PASSWORD = '219972silvia'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'
    SECRET_KEY='essentialism'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'
    # pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitchy'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yyvonne:ojijo@localhost/my_pitch'
    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yyvonne:ojijo@localhost/my-pitch_test'

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yyvonne:ojijo@localhost/my-pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}    
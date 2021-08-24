from os import path, environ
from dotenv import load_dotenv

BASE_URL = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_URL,'.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

class Development(Config):
    DEBUG = True
    TESTING = False
    ENV = 'development'

class Production(Config):
    DEBUG = False
    TESTING = False
    ENV = 'production'
import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False

class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = 'localhost:5000'  # Set SERVER_NAME
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for testing

config = {
    'testing': TestingConfig,
    'default': Config
}

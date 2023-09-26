import os

class Config:
    SECRET_KEY = 'Pollo Loco'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    #SQLALCHEMY_DATABASE_URL='postgres://eixfqopkgxcsej:8d12c7f6c3c3d158e3e1f8c8e1a80da0cb7e2af57c20ae3a631a08ef6cc70e80@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d95ealmg363pi7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
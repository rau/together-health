import os
from os import environ
from pathlib import Path
from dotenv import load_dotenv
from datetime import date
from json import load as json_load

basedir = Path(__file__).resolve().parent
load_dotenv(basedir / '.env')

class Config:
    """Sets Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG", "false").lower() == "true"
    if environ.get("FLASK_APP"):
        FLASK_APP = environ.get("FLASK_APP")

    # Automatically reloads templates upon editing of app
    TEMPLATES_AUTO_RELOAD = True
    # Sets root path of directory to actual root path
    ROOT_PATH = basedir

    CSRF_DISABLE = True
    SESSION_COOKIE_SAMESITE = None
    REMEMBER_COOKIE_SECURE = True

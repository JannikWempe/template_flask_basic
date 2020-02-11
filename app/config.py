import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Dev:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = os.environ.get("TESTING")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

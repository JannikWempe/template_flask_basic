import os


class DefaultConfig(object):
    """Default Flask config for all environments."""

    PROJECT_NAME = "StoreLayouter"
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class DevelopmentConfig(DefaultConfig):
    """Flask config for development environment."""

    TESTING = True
    FLASK_DEBUG = True


class ProductionConfig(DefaultConfig):
    """Flask config for production environment."""

    TESTING = False
    FLASK_DEBUG = False


# FLASK_ENV must be set to one of the keys in order to select the correct config
configurations = {"production": ProductionConfig, "development": DevelopmentConfig}

import os


class DefaultConfig(object):
    """Default Flask config for all environments."""

    @property
    def PROJECT_NAME(self):
        return os.environ.get("PROJECT_NAME")

    @property
    def SECRET_KEY(self):
        return os.environ.get("SECRET_KEY")

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return os.environ.get("SQLALCHEMY_DATABASE_URI")


class DevelopmentConfig(DefaultConfig):
    """Flask config for development environment."""

    TESTING = True
    FLASK_DEBUG = True


class ProductionConfig(DefaultConfig):
    """Flask config for production environment."""

    TESTING = False
    FLASK_DEBUG = False

    @property
    def BASIC_AUTH_USERNAME(self):
        return os.environ.get("BASIC_AUTH_USERNAME")

    @property
    def BASIC_AUTH_PASSWORD(self):
        return os.environ.get("BASIC_AUTH_PASSWORD")


# FLASK_ENV must be set to one of the keys in order to select the correct config
configurations = {"production": ProductionConfig, "development": DevelopmentConfig}

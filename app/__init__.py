import os

from flask_api import FlaskAPI
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from dotenv import load_dotenv

from app.config import configurations as c

db = SQLAlchemy()


def create_app(testing=False):
    flask_env = os.environ.get("FLASK_ENV")
    if not flask_env or flask_env not in c.keys():
        raise Exception(
            f"Environment variable FLASK_ENV must be set to one of the following values: {', '.join(c.keys())}."
        )
    config = c.get(flask_env, None)
    if not config:
        raise Exception(f"Config for {flask_env} could not be loaded.")

    dotenv_path = os.path.join(os.path.dirname(__file__), f".env.{flask_env}")
    load_dotenv(dotenv_path, verbose=True)

    app = FlaskAPI(__name__)

    config_instance = config()  # needed to run the config class and populate properties
    app.config.from_object(config_instance)
    if config_instance.DEBUG:
        print_used_config(app)

    db.init_app(app)
    if flask_env == "production":
        CORS(None)  # TODO: specify CORS for production use
        BasicAuth(app)
    else:
        CORS(app)  # Access-Control-Allow-Origin: '*' by default

    with app.app_context():
        from .blog.routes import blog_bp

        app.register_blueprint(blog_bp, url_prefix="/blog", cli_group="blog")
        return app


def print_used_config(app):
    print("USED CONFIG VALUES:")
    ordered_used_config = sorted(app.config.items(), key=lambda el: el[0])
    for single_config in ordered_used_config:
        print(single_config)

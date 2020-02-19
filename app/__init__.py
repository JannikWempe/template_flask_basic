import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)
    db.init_app(app)

    with app.app_context():
        from .blog.routes import blog_bp

        app.register_blueprint(blog_bp, url_prefix="/blog", cli_group="blog")
        return app

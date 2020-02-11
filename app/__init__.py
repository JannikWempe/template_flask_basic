from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(testing=False):
    from .blog.routes import blog_bp

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app.config.Dev")

    db.init_app(app)

    with app.app_context():
        app.register_blueprint(blog_bp, url_prefix="/blog", cli_group="blog")
        return app

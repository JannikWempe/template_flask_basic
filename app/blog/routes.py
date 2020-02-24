from flask import Blueprint, jsonify
from flask_api import status, exceptions

from .models import BlogPost

# Set up a Blueprint
blog_bp = Blueprint("blog_bp", __name__, template_folder="templates", static_folder="static")

from .cli import *  # noqa


@blog_bp.route("/", methods=["GET"])
def index():
    """Get all blogs."""
    blogs = BlogPost.query.all()
    blog_as_dict = [blog.as_dict() for blog in blogs]
    print(blog_as_dict)
    return jsonify({"blogposts": blog_as_dict}), status.HTTP_200_OK


@blog_bp.route("/<int:id>", methods=["GET"])
def blogpost(id):
    """Get specific blog by id."""
    print(id)
    blog = BlogPost.by_id(id)
    if not blog:
        raise exceptions.NotFound()
    return jsonify(blog.as_dict()), status.HTTP_200_OK

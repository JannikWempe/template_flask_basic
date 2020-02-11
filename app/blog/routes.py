from flask import Blueprint, render_template


# Set up a Blueprint
blog_bp = Blueprint("blog_bp", __name__, template_folder="templates", static_folder="static")

from .cli import *  # noqa


@blog_bp.route("/", methods=["GET"])
def blog_index():
    """Admin page route."""
    return render_template("index.html")

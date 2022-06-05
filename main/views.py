"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    Views from main blueprint
"""

from flask import Blueprint, render_template, request
import logging


from app_posts import Posts
from grm import WebAppError


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
posts = Posts()
logger = logging.getLogger("search")


@main_blueprint.route("/")
def main_index():
    return render_template("index.html")


@main_blueprint.route("/post_list")
def main_post_list():
    substring = request.args.get("s")
    if substring:
        raw_posts = posts.select_by_content(substring)
    else:
        raw_posts = posts.select_all()
    logger.info(f"search for the substring \"{substring}\"")
    return render_template("post_list.html", substring=substring, posts=raw_posts)


@main_blueprint.errorhandler(WebAppError)
def main_error(e):
    return f"<h1>ERROR {e.code}</h1><p>{e.msg}</p>", e.code

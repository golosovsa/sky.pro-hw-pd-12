"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    Views from loader blueprint
"""


from flask import Blueprint, render_template, request, send_from_directory, url_for
import logging


from app_pictures import Pictures
from app_posts import Posts
from grm import WebAppError


loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
pictures = Pictures()
posts = Posts()
logger_info = logging.getLogger("upload")
logger_error = logging.getLogger("upload_error")


@loader_blueprint.route("/post_form")
def loader_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post_uploaded", methods=["POST"])
def loader_uploaded():
    picture = request.files.get("picture")
    content = request.values.get("content")

    if not picture:
        raise WebAppError(400, "Upload picture failed.")
    if not Pictures.check_extension(picture.filename):
        logger_info.info(f"Invalid picture extension ({picture.filename})")
        raise WebAppError(400, "Invalid picture extension.")
    if not content or len(content) == 0:
        raise WebAppError(400, "You are trying to add empty content")

    hashed_filename = pictures.upload(picture)
    hashed_filename_uri = url_for("loader_blueprint.loader_uploads", path=hashed_filename)
    posts.insert_new(hashed_filename_uri, content)

    return render_template("post_uploaded.html", pic=hashed_filename_uri, content=content)


@loader_blueprint.route("/uploads/<path:path>")
def loader_uploads(path):
    return send_from_directory(pictures.directory, path)


@loader_blueprint.errorhandler(WebAppError)
def loader_error(e):
    logger_error.error(f"Error {e.code} - {e.msg}")
    return f"<h1>ERROR {e.code}</h1><p>{e.msg}</p>", e.code


@loader_blueprint.errorhandler(413)
def loader_file_too_large(e):
    logger_error.error(f"Error {e.code} - {e.description}")
    return f"<h1>ERROR {e.code}</h1><p>{e.description}</p>", e.code

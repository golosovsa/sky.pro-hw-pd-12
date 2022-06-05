"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    App file
"""


from flask import Flask
from main.views import main_blueprint
from loader.views import loader_blueprint


import settings
from app_posts import Posts
from app_pictures import Pictures
from loggers import init_loggers


app = Flask(__name__)
posts = Posts()
pictures = Pictures()
init_loggers()


app.config.update({
    "UPLOAD_FOLDER": settings.APP_STORAGE,
    "MAX_CONTENT_LENGTH": settings.APP_STORAGE_MAX_FILE_SIZE,
    "UPLOAD_EXTENSIONS": settings.APP_STORAGE_EXTENSIONS,
})

app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(loader_blueprint, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True)


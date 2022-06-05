"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    Pictures singleton class file
"""


from werkzeug.datastructures import FileStorage
from pathlib import Path


from grm import FolderStorage
import settings


class Pictures(FolderStorage):
    """ Pictures singleton class """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super(Pictures, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super(Pictures, self).__init__(Path(settings.APP_STORAGE))

    def upload(self, new_picture: FileStorage):
        """ Upload new picture

        :param new_picture: FileStorage object from POST method
        :return: New hash name of the added picture
        """

        hashed_filename = self.get_hashed_name(new_picture)

        if not self.is_exists(hashed_filename):
            self.insert_new(new_picture, hashed_filename)

        return hashed_filename

    @property
    def directory(self):
        return str(self._source)

    @staticmethod
    def check_extension(filename: str) -> bool:
        ext = "." + filename.rstrip().rsplit(".", 1)[-1].lower()
        return ext in settings.APP_STORAGE_EXTENSIONS

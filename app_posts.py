"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    Posts singleton class file
"""


from grm import JSONDatabase
from pathlib import Path


import settings


class Posts(JSONDatabase):
    """ Posts singleton class """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super(Posts, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super(Posts, self).__init__(Path(settings.APP_DATA))

    def select_by_content(self, substring: str) -> list[dict]:
        """ Select posts by content substring filtration

        :param substring: Content substring
        :return: List of posts
        """
        def is_substring(source, dest):
            return dest.strip().lower() in source.strip().lower()
        return self.select_by_field("content", substring, is_substring)

    def insert_new(self, pic: str, content: str):
        """ Insert new post into database

        :param pic: Picture URI
        :param content: Text content
        """
        data = self.select_all()
        data.append(dict(pic=pic, content=content))
        self.update_all(data)

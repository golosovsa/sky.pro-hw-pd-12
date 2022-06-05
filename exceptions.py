"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    Exception classes file
"""


from grm import WebAppError


class InvalidFileExtension(WebAppError):
    def __init__(self, ext):
        super(InvalidFileExtension, self).__init__(500, f"Invalid file extension {ext}")

"""
    Homework №12
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050

    Loggers init function
"""


import logging


def init_loggers():
    """ Init loggers for web app
    
    1. 'info' - when searching
    2. 'info' - if the uploaded file is not an image
    3. 'error' - if file upload error
    
    """

    # formatters

    info_formatter = logging.Formatter("%(asctime)s : %(message)s")
    error_formatter = logging.Formatter("%(pathname)s : %(funcName)s : %(asctime)s : %(message)s")

    # console handlers

    info_console_handler = logging.StreamHandler()
    info_console_handler.setFormatter(info_formatter)

    error_console_handler = logging.StreamHandler()
    error_console_handler.setFormatter(error_formatter)

    # file handlers

    info_file_handler_search = logging.FileHandler("logs/search.log")
    info_file_handler_search.setFormatter(info_formatter)

    info_file_handler_upload = logging.FileHandler("logs/upload.log")
    info_file_handler_upload.setFormatter(info_formatter)

    error_file_handler_upload = logging.FileHandler("logs/upload_errors.log")
    error_file_handler_upload.setFormatter(error_formatter)

    # 1. logger "search"

    logger = logging.getLogger("search")
    logger.setLevel(logging.INFO)
    logger.addHandler(info_console_handler)
    logger.addHandler(info_file_handler_search)

    # 2. logger "upload"

    logger = logging.getLogger("upload")
    logger.setLevel(logging.INFO)
    logger.addHandler(info_console_handler)
    logger.addHandler(info_file_handler_upload)

    # 3. logger "upload_error"

    logger = logging.getLogger("upload_error")
    logger.setLevel(logging.ERROR)
    logger.addHandler(error_console_handler)
    logger.addHandler(error_file_handler_upload)

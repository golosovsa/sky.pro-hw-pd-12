"""
    Folder storage module from grm package
"""


from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from pathlib import Path


from .utils import try_list_dir, try_os_io, fast_hash
import settings


class FolderStorage:
    """ Folder storage class """

    def __init__(self, source):
        self._source = source

    def select_all(self, pattern: str = "*") -> list[Path]:
        """ Select all files, filtered by GLOB pattern

        Can raise exceptions WebServerOSError, AttemptsExceededError

        :param pattern: GLOB pattern
        :return: List of Path objects
        """
        return try_list_dir(self._source, pattern, settings.APP_STORAGE_MAX_ATTEMPTS, settings.APP_STORAGE_SLEEP_FOR)

    @try_os_io(attempts=settings.APP_STORAGE_MAX_ATTEMPTS, sleep_for=settings.APP_STORAGE_SLEEP_FOR)
    def delete_by_name(self, name: Path):
        """ Delete file by name

        Can raise exceptions WebServerOSError, AttemptsExceededError

        :param name:
        """
        path = self._source.joinpath(name.name)
        path.unlink()

    @staticmethod
    def get_hashed_name(new_file: FileStorage) -> str:
        """ Get hashed file name with suffix

        :param new_file: FileStorage object from POST method
        :return: Hashed file name with suffix
        """
        filename = secure_filename(new_file.filename)
        file_ext = filename.rstrip().rsplit(".", 1)[-1].lower()
        hashed = fast_hash(new_file.read())
        filename = f"{hashed}.{file_ext}"
        return filename

    def is_exists(self, hashed_name: str) -> bool:
        """ Is file with hashed name exists

        Can raise exceptions WebServerOSError, AttemptsExceededError

        :param hashed_name: Hashed file name with suffix
        :return: True or False
        """
        all_files = [p.name for p in self.select_all("*")]
        return hashed_name in all_files

    @try_os_io(attempts=settings.APP_STORAGE_MAX_ATTEMPTS, sleep_for=settings.APP_STORAGE_SLEEP_FOR)
    def insert_new(self, new_file: FileStorage, filename: str):
        """ Insert new file into storage

        Can raise exceptions WebServerOSError, AttemptsExceededError

        :param new_file: FileStorage object
        :param filename: Filename
        """
        new_file.stream.seek(0)
        new_file.save(str(self._source.joinpath(filename)))


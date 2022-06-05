"""
    Utils module from grm package
"""


import errno
from pathlib import Path
from time import sleep
import xxhash


from .exceptions import AttemptsExceededError, WebServerOSError


def try_open(path: Path, mode: str, encoding: str = "utf-8", attempts: int = 10, sleep_for: float = 0.2) -> object:
    """ Try open file for a few attempts

    Can raise exceptions WebServerOSError, AttemptsExceededError

    :param path: Path object for source file
    :param mode: File open mode
    :param encoding: Source file encoding (default 'utf-8')
    :param attempts: Number of attempts (default 10)
    :param sleep_for: Sleep time between attempts (default 0.2 second)
    :return: file stream object
    """

    attempt = 0

    while attempt < attempts:
        attempt += 1

        try:
            file_descriptor = path.open(mode, encoding=encoding)

        except OSError as e:
            if e.errno != errno.EBUSY:
                raise WebServerOSError(e.errno)
            sleep(sleep_for)
            continue

        return file_descriptor

    raise AttemptsExceededError()


def try_list_dir(path: Path, pattern: str = '*', attempts: int = 10, sleep_for: float = 0.2) -> list[Path]:
    """ Try to get a list of files from directory for few attempts

    Can raise exceptions WebServerOSError, AttemptsExceededError

    :param path: Path object for source file
    :param pattern: GLOB pattern to filtrate output list of files (default '*')
    :param attempts: Number of attempts (default 10)
    :param sleep_for: Sleep time between attempts (default 0.2 second)
    :return: List of Paths
    """

    attempt = 0

    while attempt < attempts:
        attempt += 1

        try:
            return path.glob(pattern)

        except OSError as e:
            if e.errno != errno.EBUSY:
                raise WebServerOSError(e.errno)
            sleep(sleep_for)
            continue

    raise AttemptsExceededError()


def try_os_io(attempts: int = 10, sleep_for: float = 0.2):
    """ Try manipulating os io functions class method decorator

    Can raise exceptions WebServerOSError, AttemptsExceededError

    :param attempts: Number of attempts (default 10)
    :param sleep_for: sleep_for: Sleep time between attempts (default 0.2 second)
    :return:
    """

    def decorate(function):

        def wrapper(self, *args):

            attempt = 0
            while attempt < attempts:
                attempt += 1
                try:
                    return function(self, *args)

                except OSError as e:
                    if e.errno != errno.EBUSY:
                        raise WebServerOSError(e.errno)
                    sleep(sleep_for)
                    continue

            raise AttemptsExceededError()

        return wrapper

    return decorate


def fast_hash(binary):
    """ Fast hash function

    :param binary: Binary data
    :return: Hex digest string
    """
    return xxhash.xxh64(binary).hexdigest()

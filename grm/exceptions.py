"""
    Exceptions module from grm package
"""


class WebAppError(Exception):
    def __init__(self, code, msg):
        self._code = code
        self._msg = msg
        super().__init__(self._msg)

    def __str__(self):
        return f"{self._msg} - ({self._code})"

    @property
    def code(self):
        return self._code

    @property
    def msg(self):
        return self._msg


class AttemptsExceededError(WebAppError):
    def __init__(self):
        super(AttemptsExceededError, self).__init__(503, "Exceeded number of attempts to open resource.")


class WebServerOSError(WebAppError):
    def __init__(self, errno):
        super(WebServerOSError, self).__init__(500, f"Server OS error. errno={errno}.")


class JSONDatabaseError(WebAppError):
    def __init__(self):
        super(JSONDatabaseError, self).__init__(500, f"App file JSON data structure is corrupted.")

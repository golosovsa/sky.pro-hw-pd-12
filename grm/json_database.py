"""
    JSON Database module from grm package
"""

import json
import operator
from pathlib import Path

from .exceptions import JSONDatabaseError
from .utils import try_open
import settings


class JSONDatabase:
    """ JSON Database class"""

    def __init__(self, source: Path):
        self._source = source

    def select_all(self):
        """ Select all records from database

        Can raise exceptions JSONDatabaseError, WebServerOSError, AttemptsExceededError

        :return: List of records
        """
        try:
            with try_open(
                    self._source,
                    "rt",
                    attempts=settings.APP_DATA_MAX_ATTEMPTS,
                    sleep_for=settings.APP_DATA_SLEEP_FOR) as fin:
                return json.load(fin)

        except json.JSONDecodeError:
            raise JSONDatabaseError()

    def select_by_field(self, field: str, value: any, compare=operator.eq):
        """ Select records from database by filed

        Can raise exceptions: JSONDatabaseError, WebServerOSError, AttemptsExceededError

        :param field: Record field name
        :param value: Value for comparison
        :param compare: Comparison function
        :return: List of records (can be empty list)
        """
        data = self.select_all()

        try:
            result = [record for record in data if compare(record[field], value)]

        except KeyError:
            raise JSONDatabaseError()

        return result

    def select_one_by_field(self, field: str, value: any, compare=operator.eq):
        """ Select first record by field or None

        Can raise exceptions: JSONDatabaseError, WebServerOSError, AttemptsExceededError

        :param field: Record field name
        :param value: Value for comparison
        :param compare: Comparison function
        :return: The record or None
        """

        data = self.select_all()

        try:
            for record in data:
                if compare(record[field], value):
                    return record

        except KeyError:
            raise JSONDatabaseError()

        return None

    def update_one_by_field(self, field, value, upd_record, compare=operator.eq):
        """ Update or add record by field

        Can raise exceptions: JSONDatabaseError, WebServerOSError, AttemptsExceededError

        :param field: Record field name
        :param value: Value for comparison
        :param upd_record: New or updated record
        :param compare: Comparison function
        """
        data = self.select_all()

        try:
            for record in data:
                if compare(record[field], value):
                    record.update(upd_record)
                    break
            else:
                data.append(upd_record)

        except KeyError:
            raise JSONDatabaseError()

        self.update_all(data)

    def update_all(self, data):
        """ Update all records

        Can raise exceptions: JSONDatabaseError, WebServerOSError, AttemptsExceededError

        :param data: Data to update
        """
        try:
            with try_open(
                    self._source,
                    "wt",
                    attempts=settings.APP_DATA_MAX_ATTEMPTS,
                    sleep_for=settings.APP_DATA_SLEEP_FOR) as fou:
                json.dump(data, fou, ensure_ascii=False)

        except json.JSONDecodeError:
            raise JSONDatabaseError()

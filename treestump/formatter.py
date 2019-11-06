import json
import logging
import socket


class TreestumpFormatter(logging.Formatter):
    def __init__(self, application: str, *args, **kwargs):
        """
        @param application: the name of the application using the logger
        @type application: str
        """
        super().__init__(*args, **kwargs)
        self.application = application
        self.host = socket.gethostname()

    def _json_format(self, log_record: logging.LogRecord) -> dict:
        """
        Defines the dictionary ready to be dumped as JSON.

        This method collects basic useful information from the Python logging.LogRecord object. It is designed to be extended by subclasses calling `super()` to extend the dictionary with application specific logging information. This allows developers to easily modify the log message *before* it is dumped as JSON, and prevents the user from needing to override the `format` method itself.

        @note This method should only be called by `TreestumpFormatter.format()`
        @param record: The log record that needs to be formatted as JSON
        @type record: logging.LogRecord
        @return: A dictionary containing specific record items, ready to be dumped as JSON
        @rtype: dict
        """
        exception = log_record.exc_info
        record_dict = {
            "timestamp": log_record.created,
            "message": log_record.getMessage(),
            "host": self.host,
            "application": self.application,
            "type": "exception" if exception else "log",
            "level": log_record.levelname,
            "levelNumber": log_record.levelno,
            "logger": log_record.name,
            "path": log_record.pathname,
            "filename": log_record.filename,
            "module": log_record.module,
            "function": log_record.funcName,
            "line": log_record.lineno,
            "processId": log_record.process,
            "processName": log_record.processName,
            "threadName": log_record.threadName,
            "stackInfo": self.formatStack(
                log_record.stack_info
            ),  # this may be too verbose - need feedback from folks
        }
        if exception:
            record_dict.update({"trace": "".join(self.FormatException(exception))})
        return record_dict

    def format(self, log_record: logging.LogRecord) -> str:
        """
        @param log_record: the incoming Python logging.LogRecord object
        @type log_record: logging.LogRecord
        @return: JSON formatted string containing log record information
        @rtype: str
        """
        return json.dumps(self._json_format(log_record), ensure_ascii=False)

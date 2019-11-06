from io import StringIO
import json
import logging
from unittest import mock

import pytest

from treestump.formatter import TreestumpFormatter
from treestump.logger import TreestumpLogger


class TestTreestumpLogger:
    @pytest.fixture
    def test_stream(self):
        return StringIO()

    @pytest.fixture
    def test_logger(self, test_stream):
        logger = TreestumpLogger("sample")
        handler = logging.StreamHandler(test_stream)
        handler.setFormatter(TreestumpFormatter("sample"))
        logger._logger.addHandler(handler)
        return logger

    def test_logger_default_formatter(self, test_logger):
        assert test_logger.event_log_formatter_cls == TreestumpFormatter

    def test_logger_app_name(self, test_logger):
        assert test_logger.app_name == "sample"

    def test_logger_repr(self, test_logger):
        assert test_logger.__repr__() == "TreestumpLogger for application 'sample'"

    def test_logger_default_log_level_message(self, test_logger, test_stream):
        message = "sample message"
        test_logger.log(message)
        logged_message = json.loads(test_stream.getvalue())
        assert logged_message["message"] == message
        assert logged_message["level"] == "INFO"
        assert logged_message["levelNumber"] == 20

    def test_logger_custom_log_level_message(self, test_logger, test_stream):
        message = "sample message"
        test_logger.log(message, 50)
        logged_message = json.loads(test_stream.getvalue())
        assert logged_message["message"] == message
        assert logged_message["level"] == "CRITICAL"
        assert logged_message["levelNumber"] == 50

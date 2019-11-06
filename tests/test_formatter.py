import json
import logging
from unittest import mock

import pytest

from treestump.formatter import TreestumpFormatter


class TestTreestumpFormatter:
    @pytest.fixture
    @mock.patch("treestump.formatter.socket.gethostname")
    def test_formatter(self, mock_hostname):
        mock_hostname.return_value = "sample-host.123"
        return TreestumpFormatter("sample")

    @pytest.fixture
    def test_record(self):
        return logging.LogRecord(
            "sample", 20, "~/", "12", "sample message", [123], None
        )

    def test_formatter_attributes(self, test_formatter):
        assert test_formatter.application == "sample"
        assert test_formatter.host == "sample-host.123"

    def test_returns_valid_json(self, test_formatter, test_record):
        output = test_formatter.format(test_record)
        assert isinstance(output, str)
        assert isinstance(json.loads(output), dict)

# -*- coding: utf-8 -*-

import os

from lintaosp.aosp.strings import Strings, StringsException
from lintaosp.config.config import Config


def test_exception():
    exception = StringsException("exception")
    assert str(exception) == "exception"


def test_strings():
    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    data = "PHN0cmluZyBuYW1lPSJsaW50X2Fvc3AiPkxpbnQgQU9TUDwvc3RyaW5nPg=="

    try:
        strings = Strings(config)
        result = strings._execution(data)
    except StringsException as _:
        assert False
    else:
        assert True

    assert result is not None

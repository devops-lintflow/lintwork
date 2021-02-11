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

    try:
        strings = Strings(config)
        _exec = strings._execution()
    except StringsException as _:
        assert False
    else:
        assert True

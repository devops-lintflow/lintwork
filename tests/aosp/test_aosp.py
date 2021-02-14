# -*- coding: utf-8 -*-

import os

from lintaosp.aosp.aosp import Aosp, AospException
from lintaosp.config.config import Config


def test_exception():
    exception = AospException("exception")
    assert str(exception) == "exception"


def test_aosp():
    try:
        _ = Aosp(None)
    except AospException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")
    config.output_file = "output.json"

    try:
        aosp = Aosp(config)
    except AospException as _:
        assert False
    else:
        assert True

    data = "PHN0cmluZyBuYW1lPSJsaW50X2Fvc3AiPkxpbnQgQU9TUDwvc3RyaW5nPg=="

    try:
        buf = aosp.routine(data)
    except AospException as _:
        assert False
    else:
        assert True

    assert buf is not None

    assert os.path.isfile(config.output_file)
    os.remove(config.output_file)

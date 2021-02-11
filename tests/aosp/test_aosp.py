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
    config.output_file = ""

    try:
        aosp = Aosp(config)
    except AospException as _:
        assert False
    else:
        assert True

    assert aosp._instance() is not None

    try:
        buf = aosp.routine(host=None, spec=None)
    except AospException as _:
        assert False
    else:
        assert True

    assert buf is not None

    try:
        buf = aosp.routine(host="foo", spec=None)
    except AospException as _:
        assert False
    else:
        assert True

    assert buf is not None
    assert len(buf.keys()) == 0

    try:
        buf = aosp.routine(host="bare", spec=None)
    except AospException as _:
        assert False
    else:
        assert True

    assert buf["bare"] is not None

    try:
        buf = aosp.routine(host="bare", spec="foo")
    except AospException as _:
        assert False
    else:
        assert True

    assert buf["bare"]["foo"] is None

    config.output_file = "output.json"

    try:
        buf = aosp.routine(host="bare", spec="cpu")
    except AospException as _:
        assert False
    else:
        assert True

    assert buf["bare"]["cpu"] is not None

    assert os.path.isfile(config.output_file)
    os.remove(config.output_file)

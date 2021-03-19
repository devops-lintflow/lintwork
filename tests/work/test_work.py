# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config
from lintwork.work.work import Work, WorkException


def test_exception():
    exception = WorkException("exception")
    assert str(exception) == "exception"


def test_work():
    try:
        _ = Work(None)
    except WorkException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )
    config.output_file = "output.json"

    try:
        work = Work(config)
    except WorkException as _:
        assert False
    else:
        assert True

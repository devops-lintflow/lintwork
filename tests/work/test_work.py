# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config
from lintwork.format.format import Type
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

    lint = "lintshell"

    reports = [
        {"file": "file1", "line": 1, "type": Type.ERROR, "details": "details1"},
        {"file": "file2", "line": 2, "type": Type.WARN, "details": "details2"},
    ]

    work._dump(lint, reports)
    assert os.path.isfile(config.output_file)
    os.remove(config.output_file)

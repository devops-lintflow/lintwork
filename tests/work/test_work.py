# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config
from lintwork.format.format import Type
from lintwork.work.work import Work, WorkException


class LintReport:
    file = ""
    line = ""
    type = ""
    details = ""


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

    report1 = LintReport()
    report1.file = "file1"
    report1.line = 1
    report1.type = Type.ERROR
    report1.details = "details1"

    report2 = LintReport()
    report2.file = "file2"
    report2.line = 2
    report2.type = Type.WARN
    report2.details = "details2"

    reports = [report1, report2]

    work._dump(lint, reports)
    assert os.path.isfile(config.output_file)
    os.remove(config.output_file)

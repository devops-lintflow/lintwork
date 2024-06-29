# -*- coding: utf-8 -*-

import os

from lintwork.work.lintshell.shellcheck import Shellcheck, ShellcheckException


def test_exception():
    exception = ShellcheckException("exception")
    assert str(exception) == "exception"


def test_shellcheck():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/lintshell/shellcheck.txt"),
        "r",
    ) as f:
        data = f.read()

    try:
        shellcheck = Shellcheck([])
        buf = shellcheck._parse(data)
    except ShellcheckException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

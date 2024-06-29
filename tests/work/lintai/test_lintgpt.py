# -*- coding: utf-8 -*-

import os

from lintwork.work.lintai.lintgpt import Lintgpt, LintgptException


def test_exception():
    exception = LintgptException("exception")
    assert str(exception) == "exception"


def test_lintgpt():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/lintai/lintgpt.txt"), "r"
    ) as f:
        data = f.read()

    try:
        lintgpt = Lintgpt([])
        buf = lintgpt._parse(data)
    except LintgptException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

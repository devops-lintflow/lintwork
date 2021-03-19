# -*- coding: utf-8 -*-

import os

from lintwork.work.aosp.lint import Lint, LintException


def test_exception():
    exception = LintException("exception")
    assert str(exception) == "exception"


def test_lint():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/aosp/lint.txt"), "r"
    ) as f:
        data = f.read()

    try:
        lint = Lint([])
        buf = lint._parse(data)
    except LintException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

# -*- coding: utf-8 -*-

import os

from lintwork.work.java.checkstyle import Checkstyle, CheckstyleException


def test_exception():
    exception = CheckstyleException("exception")
    assert str(exception) == "exception"


def test_checkstyle():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/java/checkstyle.txt"), "r"
    ) as f:
        data = f.read()

    try:
        checkstyle = Checkstyle([])
        buf = checkstyle._parse(data)
    except CheckstyleException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

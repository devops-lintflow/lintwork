# -*- coding: utf-8 -*-

from lintwork.work.java.checkstyle import Checkstyle, CheckstyleException


def test_exception():
    exception = CheckstyleException("exception")
    assert str(exception) == "exception"


def test_checkstyle():
    with open("../../data/java/checkstyle.txt", "r") as f:
        data = f.read()

    try:
        checkstyle = Checkstyle([])
        buf = checkstyle._parse(data)
    except CheckstyleException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

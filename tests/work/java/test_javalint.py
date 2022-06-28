# -*- coding: utf-8 -*-

import os

from lintwork.work.java.javalint import Javalint, JavalintException


def test_exception():
    exception = JavalintException("exception")
    assert str(exception) == "exception"


def test_javalint():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/java/javalint.txt"), "r"
    ) as f:
        data = f.read()

    try:
        javalint = Javalint([])
        buf = javalint._parse(data)
    except JavalintException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

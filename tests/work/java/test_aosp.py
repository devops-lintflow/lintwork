# -*- coding: utf-8 -*-

import os

from lintwork.work.java.aosp import Aosp, AospException


def test_exception():
    exception = AospException("exception")
    assert str(exception) == "exception"


def test_aosp():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/java/aosp.txt"), "r"
    ) as f:
        data = f.read()

    try:
        aosp = Aosp([])
        buf = aosp._parse(data)
    except AospException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

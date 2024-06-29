# -*- coding: utf-8 -*-

import os

from lintwork.work.lintjava.aosplint import Aosplint, AosplintException


def test_exception():
    exception = AosplintException("exception")
    assert str(exception) == "exception"


def test_aosplint():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/lintjava/aosplint.txt"), "r"
    ) as f:
        data = f.read()

    try:
        aosplint = Aosplint([])
        buf = aosplint._parse(data)
    except AosplintException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

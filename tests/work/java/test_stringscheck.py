# -*- coding: utf-8 -*-

import os

from lintwork.work.java.stringscheck import Stringscheck, StringscheckException


def test_exception():
    exception = StringscheckException("exception")
    assert str(exception) == "exception"


def test_stringscheck():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/java/stringscheck.txt"),
        "r",
    ) as f:
        data = f.read()

    try:
        stringscheck = Stringscheck([])
        buf = stringscheck._parse(data)
    except StringscheckException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

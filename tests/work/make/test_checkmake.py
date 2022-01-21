# -*- coding: utf-8 -*-

import os

from lintwork.work.make.checkmake import Checkmake, CheckmakeException


def test_exception():
    exception = CheckmakeException("exception")
    assert str(exception) == "exception"


def test_checkmake():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/make/checkmake.txt"), "r"
    ) as f:
        data = f.read()

    try:
        checkmake = Checkmake([])
        buf = checkmake._parse("checkmake.txt", data)
    except CheckmakeException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

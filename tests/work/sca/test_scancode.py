# -*- coding: utf-8 -*-

import os

from lintwork.work.sca.scancode import Scancode, ScancodeException


def test_exception():
    exception = ScancodeException("exception")
    assert str(exception) == "exception"


def test_scancode():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/sca/scancode.txt"),
        "r",
    ) as f:
        data = f.read()

    try:
        scancode = Scancode([])
        buf = scancode._parse(data)
    except ScancodeException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

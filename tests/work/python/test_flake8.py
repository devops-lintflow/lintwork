# -*- coding: utf-8 -*-

import os

from lintwork.work.python.flake8 import Flake8, Flake8Exception


def test_exception():
    exception = Flake8Exception("exception")
    assert str(exception) == "exception"


def test_flake8():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/python/flake8.txt"), "r"
    ) as f:
        data = f.read()

    try:
        flake8 = Flake8([])
        buf = flake8._parse(data)
    except Flake8Exception as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

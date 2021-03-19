# -*- coding: utf-8 -*-

import os

from lintwork.work.cpp.cpplint import Cpplint, CpplintException


def test_exception():
    exception = CpplintException("exception")
    assert str(exception) == "exception"


def test_cpplint():
    config = ["--linelength=120"]

    try:
        cpplnt = Cpplint(config)
        result = cpplnt._execution(
            os.path.join(
                os.path.dirname(__file__), "../../data/cpp".replace("/", os.path.sep)
            )
        )
    except CpplintException as _:
        assert False
    else:
        assert True

    assert result is not None

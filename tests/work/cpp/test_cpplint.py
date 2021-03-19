# -*- coding: utf-8 -*-

from lintwork.work.cpp.cpplint import Cpplint, CpplintException


def test_exception():
    exception = CpplintException("exception")
    assert str(exception) == "exception"


def test_cpplint():
    with open("../../data/cpp/cpplint.txt", "r") as f:
        data = f.read()

    try:
        cpplint = Cpplint([])
        buf = cpplint._parse(data)
    except CpplintException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

# -*- coding: utf-8 -*-

import os

from lintwork.work.sca.licenseclassifier import (
    Licenseclassifier,
    LicenseclassifierException,
)


def test_exception():
    exception = LicenseclassifierException("exception")
    assert str(exception) == "exception"


def test_licenseclassifier():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/sca/licenseclassifier.txt"),
        "r",
    ) as f:
        data = f.read()

    try:
        licenseclassifier = Licenseclassifier([])
        buf = licenseclassifier._parse(data)
    except LicenseclassifierException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

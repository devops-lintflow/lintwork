# -*- coding: utf-8 -*-

import os

from lintwork.work.commit.contentcheck import Contentcheck, ContentcheckException


def test_exception():
    exception = ContentcheckException("exception")
    assert str(exception) == "exception"


def test_contentcheck():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/commit/contentcheck.txt"),
        "r",
    ) as f:
        data = f.read()

    try:
        contentcheck = Contentcheck([])
        buf = contentcheck._parse(data)
    except ContentcheckException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

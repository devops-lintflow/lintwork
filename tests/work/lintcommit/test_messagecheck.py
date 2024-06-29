# -*- coding: utf-8 -*-

import os

from lintwork.work.lintcommit.messagecheck import Messagecheck, MessagecheckException


def test_exception():
    exception = MessagecheckException("exception")
    assert str(exception) == "exception"


def test_messagecheck():
    with open(
        os.path.join(
            os.path.dirname(__file__), "../../data/lintcommit/messagecheck.txt"
        ),
        "r",
    ) as f:
        data = f.read()

    try:
        messagecheck = Messagecheck([])
        buf = messagecheck._parse(data)
    except MessagecheckException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

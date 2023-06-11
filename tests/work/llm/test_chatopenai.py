# -*- coding: utf-8 -*-

import os

from lintwork.work.llm.chatopenai import Chatopenai, ChatopenaiException


def test_exception():
    exception = ChatopenaiException("exception")
    assert str(exception) == "exception"


def test_chatopenai():
    with open(
        os.path.join(os.path.dirname(__file__), "../../data/llm/chatopenai.txt"), "r"
    ) as f:
        data = f.read()

    try:
        chatopenai = Chatopenai([])
        buf = chatopenai._parse(data)
    except ChatopenaiException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

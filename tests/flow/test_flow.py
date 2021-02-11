# -*- coding: utf-8 -*-

import os

from lintaosp.config.config import Config
from lintaosp.flow.flow import Flow, FlowException


def test_exception():
    exception = FlowException("exception")
    assert str(exception) == "exception"


def test_flow():
    try:
        _ = Flow(None)
    except FlowException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    try:
        _ = Flow(config)
    except FlowException as _:
        assert False
    else:
        assert True

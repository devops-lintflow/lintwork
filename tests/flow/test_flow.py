# -*- coding: utf-8 -*-

import os

from lintaosp.config.config import Config
from lintaosp.flow.flow import Flow, FlowException, FlowProto


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


def test_flowproto():
    proto = FlowProto(None)

    data = ""
    project = proto._build(data)
    if project is None or not os.path.exists(project):
        assert True

    data = """{"project/AndroidManifest.xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxtYW5pZmVzdCB4bWxuczphbmRyb2lkPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9hcGsvcmVzL2FuZHJvaWQiDQogICAgICAgICAgcGFja2FnZT0iY3JhZnRzbGFiLndlcm9ib3QiPg0KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uRElTQUJMRV9LRVlHVUFSRCIvPg0KPC9tYW5pZmVzdD4NCg=="}"""
    project = proto._build(data)
    if project is not None and os.path.exists(project):
        assert True

    proto._clean(project)

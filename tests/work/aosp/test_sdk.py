# -*- coding: utf-8 -*-

from lintwork.work.aosp.sdk import Sdk, SdkException


def test_exception():
    exception = SdkException("exception")
    assert str(exception) == "exception"


def test_sdk():
    with open("../../data/aosp/sdk.txt", "r") as f:
        data = f.read()

    try:
        sdk = Sdk([])
        buf = sdk._parse(data)
    except SdkException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

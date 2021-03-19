# -*- coding: utf-8 -*-

import os

from lintwork.work.aosp.sdk import Sdk, SdkException


def test_exception():
    exception = SdkException("exception")
    assert str(exception) == "exception"


def test_sdk():
    config = [
        "Correctness",
        "Correctness:Messages",
        "Security",
        "Compliance",
        "Performance",
        "Performance:Application Size",
        "Usability:Typography",
        "Usability:Icons",
        "Usability",
        "Productivity",
        "Accessibility",
        "Internationalization",
        "Internationalization:Bidirectional Text",
    ]

    try:
        sdk = Sdk(config)
        result = sdk._execution(
            os.path.join(
                os.path.dirname(__file__), "../../data/aosp".replace("/", os.path.sep)
            )
        )
    except SdkException as _:
        assert False
    else:
        assert True

    assert result is not None

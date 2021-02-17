# -*- coding: utf-8 -*-

import os

from lintaosp.aosp.sdk import Sdk, SdkException
from lintaosp.config.config import Config


def test_exception():
    exception = SdkException("exception")
    assert str(exception) == "exception"


def test_sdk():
    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    try:
        sdk = Sdk(config)
        result = sdk._execution(
            os.path.join(os.path.dirname(__file__), "../data/project")
        )
    except SdkException as _:
        assert False
    else:
        assert True

    assert result is not None

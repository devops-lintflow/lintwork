# -*- coding: utf-8 -*-

from lintaosp.aosp.abstract import AospAbstract
from lintaosp.config.config import Config


def test_aospabstract():
    class AospTest(AospAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self):
            return {"cpu": "1CPU"}

    config = Config()
    aosp = AospTest(config)

    result = aosp.run("foo")
    assert result is None

    result = aosp.run("cpu")
    assert result is not None

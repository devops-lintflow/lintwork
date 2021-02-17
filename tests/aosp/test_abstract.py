# -*- coding: utf-8 -*-

import os

from lintaosp.aosp.abstract import AospAbstract
from lintaosp.config.config import Config
from lintaosp.proto.proto import Format


def test_aospabstract():
    class AospTest(AospAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self, _):
            return {Format.FILE: "name"}

    config = Config()
    aosp = AospTest(config)

    result = aosp.run(os.path.join(os.path.dirname(__file__), "../data/project"))
    assert result is not None

# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config
from lintwork.proto.proto import Format
from lintwork.work.abstract import WorkAbstract


def test_workabstract():
    class WorkTest(WorkAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self, _):
            return {Format.FILE: "name"}

    config = Config()
    work = WorkTest(config)

    result = work.run(os.path.join(os.path.dirname(__file__), "../data/project"))
    assert result is not None

# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config
from lintwork.format.format import Report
from lintwork.work.abstract import WorkAbstract


def test_workabstract():
    class WorkTest(WorkAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self, _):
            return {Report.FILE: "name"}

    config = Config()
    work = WorkTest(config)

    result = work.run(
        os.path.join(
            os.path.dirname(__file__), "../data/java".replace("/", os.path.sep)
        )
    )
    assert result is not None

# -*- coding: utf-8 -*-

import os

from lintwork.config.config import ConfigFile
from lintwork.printer.printer import Printer
from lintwork.work.lintai.lintgpt import Lintgpt  # noqa: F401
from lintwork.work.lintcommit.contentcheck import Contentcheck  # noqa: F401
from lintwork.work.lintcommit.messagecheck import Messagecheck  # noqa: F401
from lintwork.work.lintcpp.cpplint import Cpplint  # noqa: F401
from lintwork.work.lintjava.aosplint import Aosplint  # noqa: F401
from lintwork.work.lintjava.checkstyle import Checkstyle  # noqa: F401
from lintwork.work.lintjava.javalint import Javalint  # noqa: F401
from lintwork.work.lintjava.stringscheck import Stringscheck  # noqa: F401
from lintwork.work.lintkernel.checkpatch import Checkpatch  # noqa: F401
from lintwork.work.lintmake.checkmake import Checkmake  # noqa: F401
from lintwork.work.lintpython.flake8 import Flake8  # noqa: F401
from lintwork.work.lintsast.rapidscan import Rapidscan  # noqa: F401
from lintwork.work.lintsca.licenseclassifier import Licenseclassifier  # noqa: F401
from lintwork.work.lintshell.shellcheck import Shellcheck  # noqa: F401


class WorkException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Work(object):
    def __init__(self, config):
        if config is None:
            raise WorkException("config invalid")
        self._config = config
        self._spec = config.config_file.get(ConfigFile.SPEC, None)
        if self._spec is None:
            raise WorkException("spec invalid")

    def _dump(self, lint, reports):
        printer = Printer()
        printer.run(
            lint=lint, reports=reports, name=self._config.output_file, append=False
        )

    def routine(self, lint, project):
        if not isinstance(project, str) or not os.path.exists(project):
            raise WorkException("project invalid")
        if lint not in self._spec.keys():
            raise WorkException("lint invalid")
        reports = []
        for name, args in self._spec[lint].items():
            cls = globals().get(name.capitalize(), None)
            if cls is not None:
                reports.extend(cls(args).run(project))
        if len(self._config.output_file) != 0:
            self._dump(lint, reports)
        return reports

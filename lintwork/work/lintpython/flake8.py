# -*- coding: utf-8 -*-

import os
import subprocess

from lintwork.format.format import Report
from lintwork.work.abstract import WorkAbstract

LINT_LEN_MIN = 4
LINT_SEP = ":"


class Flake8Exception(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Flake8(WorkAbstract):
    def __init__(self, config):
        if config is None:
            config = []
        super().__init__(config)

    def _execution(self, project):
        return self._lint(project)

    def _parse(self, data):
        buf = []
        for item in data.splitlines():
            b = item.strip().split(LINT_SEP)
            if len(b) < LINT_LEN_MIN:
                continue
            buf.append(
                {
                    Report.FILE: b[0].strip(),
                    Report.LINE: int(b[1].strip()),
                    Report.TYPE: "",
                    Report.DETAILS: " ".join(b[3:]).strip(),
                }
            )
        return buf

    def _popen(self, cmd, stdin=None):
        return subprocess.Popen(
            cmd, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    def _lint(self, project):
        cmd = ["flake8"]
        cmd.extend(self._config)
        cmd.extend([project])
        with self._popen(cmd) as proc:
            out, err = proc.communicate()
            if proc.returncode == 0:
                return []
        return self._parse(
            out.strip().decode("utf-8").replace(project + os.path.sep, "")
        )

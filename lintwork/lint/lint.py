# -*- coding: utf-8 -*-

import base64
import datetime
import grpc
import os
import pathlib
import shutil

from concurrent import futures
from lintwork.lint.lint_pb2 import LintReply
from lintwork.lint.lint_pb2_grpc import (
    add_LintProtoServicer_to_server,
    LintProtoServicer,
)

LINT_PROJECT = "lintwork"
MAX_WORKERS = 10


class LintException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Lint(object):
    def __init__(self, config):
        if config is None:
            raise LintException("config invalid")
        self._config = config

    def _serve(self, routine):
        server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
            options=[
                ("grpc.max_receive_message_length", -1),
                ("grpc.max_send_message_length", -1),
            ],
        )
        add_LintProtoServicer_to_server(LintProto(routine), server)
        server.add_insecure_port(self._config.listen_url)
        server.start()
        server.wait_for_termination()

    def run(self, routine):
        self._serve(routine)


class LintProto(LintProtoServicer):
    def __init__(self, routine):
        self._routine = routine

    def _build(self, files, patch):
        def _helper(root, dir, file, content):
            pathlib.Path(os.path.join(root, dir)).mkdir(parents=True, exist_ok=True)
            p = pathlib.Path(os.path.join(root, dir, file))
            with p.open("w", encoding="utf-8") as f:
                f.write(base64.b64decode(content).decode("utf-8"))

        root = os.path.join(
            os.getcwd(),
            LINT_PROJECT + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        )
        pathlib.Path(root).mkdir(parents=True, exist_ok=True)
        for item in files:
            _helper(
                root,
                os.path.dirname(item.path),
                os.path.basename(item.path),
                item.content,
            )
        _helper(
            root,
            os.path.dirname(patch.path),
            os.path.basename(patch.path),
            patch.content,
        )

        return root

    def _clean(self, project):
        if os.path.exists(project):
            shutil.rmtree(project)

    def SendLint(self, request, _):
        if (
            len(request.name) == 0
            or len(request.lintFiles) == 0
            or len(request.lintPatch.path) == 0
        ):
            return LintReply(name="")
        project = self._build(request.lintFiles, request.lintPatch)
        if project is None or not os.path.exists(project):
            return LintReply(name="")
        reports = self._routine(request.name, project)
        self._clean(project)
        return LintReply(name=request.name, lintReports=reports)

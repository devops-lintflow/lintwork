#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc

from lint_pb2 import LintReply
from lint_pb2_grpc import (
    add_LintProtoServicer_to_server,
    LintProtoServicer,
)

from concurrent import futures


class LintProto(LintProtoServicer):
    def SendLint(self, request, _):
        if (
            request.message
            == """{"project/AndroidManifest.xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxtYW5pZmVzdCB4bWxuczphbmRyb2lkPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9hcGsvcmVzL2FuZHJvaWQiDQogICAgICAgICAgcGFja2FnZT0iY3JhZnRzbGFiLndlcm9ib3QiPg0KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uRElTQUJMRV9LRVlHVUFSRCIvPg0KPC9tYW5pZmVzdD4NCg=="}"""
        ):
            return LintReply(message="message")
        else:
            return LintReply(message="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LintProtoServicer_to_server(LintProto(), server)
    server.add_insecure_port("[::]:9090")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

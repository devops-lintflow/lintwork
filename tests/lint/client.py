#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc

from lint_pb2 import LintRequest
from lint_pb2_grpc import LintProtoStub


def run():
    channel = grpc.insecure_channel("127.0.0.1:9090")
    stub = LintProtoStub(channel)

    response = stub.SendLint(
        LintRequest(
            message="""{"project/AndroidManifest.xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxtYW5pZmVzdCB4bWxuczphbmRyb2lkPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9hcGsvcmVzL2FuZHJvaWQiDQogICAgICAgICAgcGFja2FnZT0iY3JhZnRzbGFiLndlcm9ib3QiPg0KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uRElTQUJMRV9LRVlHVUFSRCIvPg0KPC9tYW5pZmVzdD4NCg=="}"""
        )
    )
    print("client received: " + response.message)


if __name__ == "__main__":
    run()

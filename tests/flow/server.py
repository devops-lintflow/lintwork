#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc

from flow_pb2 import FlowReply
from flow_pb2_grpc import (
    add_FlowProtoServicer_to_server,
    FlowProtoServicer,
)

from concurrent import futures


class FlowProto(FlowProtoServicer):
    def SendFlow(self, request, _):
        if (
            request.message
            == """{"project/AndroidManifest.xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxtYW5pZmVzdCB4bWxuczphbmRyb2lkPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9hcGsvcmVzL2FuZHJvaWQiDQogICAgICAgICAgcGFja2FnZT0iY3JhZnRzbGFiLndlcm9ib3QiPg0KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uRElTQUJMRV9LRVlHVUFSRCIvPg0KPC9tYW5pZmVzdD4NCg=="}"""
        ):
            return FlowReply(message="message")
        else:
            return FlowReply(message="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FlowProtoServicer_to_server(FlowProto(), server)
    server.add_insecure_port("[::]:9090")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

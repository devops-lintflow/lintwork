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
            == "lintaosp/PHN0cmluZyBuYW1lPSJsaW50X2Fvc3AiPkxpbnQgQU9TUDwvc3RyaW5nPg=="
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc

from ..flow_pb2 import FlowReply
from ..flow_pb2_grpc import (
    add_FlowProtoServicer_to_server,
    FlowProtoServicer,
)

from concurrent import futures


class FlowProto(FlowProtoServicer):
    def SendFlow(self, request, _):
        return FlowReply(message="1 CPU")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FlowProtoServicer_to_server(FlowProto(), server)
    server.add_insecure_port("[::]:9090")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

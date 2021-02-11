#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc

from flow_pb2 import FlowRequest
from flow_pb2_grpc import FlowProtoStub


def run():
    channel = grpc.insecure_channel("127.0.0.1:9090")
    stub = FlowProtoStub(channel)

    response = stub.SendFlow(FlowRequest(message="lintaosp/lint/strings"))
    print("client received: " + response.message)


if __name__ == "__main__":
    run()

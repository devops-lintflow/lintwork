#!/bin/bash

src=lintaosp/flow

python -m grpc_tools.protoc -I./${src} --python_out=./${src} --grpc_python_out=./${src} ./${src}/flow.proto

# Test
# cp lintaosp/flow/flow_pb2*.py tests/flow/
# python tests/flow/server.py
# python tests/flow/client.py

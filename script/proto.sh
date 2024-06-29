#!/bin/bash

# Install protoc
# curl -LO https://github.com/protocolbuffers/protobuf/releases/download/v26.1/protoc-26.1-linux-x86_64.zip

# Build proto
src=lintwork/lint
python -m grpc_tools.protoc -I./${src} --python_out=./${src} --grpc_python_out=./${src} ./${src}/lint.proto

# Test
# cp lintwork/lint/lint_pb2*.py tests/lint/
# python tests/lint/server.py
# python tests/lint/client.py

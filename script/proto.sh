#!/bin/bash

# Install protoc
# curl -LO https://github.com/protocolbuffers/protobuf/releases/download/v28.2/protoc-28.2-linux-x86_64.zip

# Build proto
src=lintwork/lint
python -m grpc_tools.protoc -I./${src} --python_out=./${src} --grpc_python_out=./${src} ./${src}/lint.proto

# Modify proto
# lint_pb2_grpc.py
# -import lint_pb2 as lint__pb2
# +import lintwork.lint.lint_pb2 as lint__pb2

# Test
# cp lintwork/lint/lint_pb2*.py tests/lint/
# python tests/lint/server.py
# python tests/lint/client.py

#!/bin/bash

src=lintwork/lint

python -m grpc_tools.protoc -I./${src} --python_out=./${src} --grpc_python_out=./${src} ./${src}/lint.proto

# Test
# cp lintwork/lint/lint_pb2*.py tests/lint/
# python tests/lint/server.py
# python tests/lint/client.py

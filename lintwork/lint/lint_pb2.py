# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nlint.proto\x12\x04lint\"\x1e\n\x0bLintRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\tLintReply\x12\x0f\n\x07message\x18\x01 \x01(\t2=\n\tLintProto\x12\x30\n\x08SendLint\x12\x11.lint.LintRequest\x1a\x0f.lint.LintReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lint_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LINTREQUEST._serialized_start=20
  _LINTREQUEST._serialized_end=50
  _LINTREPLY._serialized_start=52
  _LINTREPLY._serialized_end=80
  _LINTPROTO._serialized_start=82
  _LINTPROTO._serialized_end=143
# @@protoc_insertion_point(module_scope)

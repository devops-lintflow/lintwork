# -*- coding: utf-8 -*-


"""Prototype
{
  "lintwork": [
    {
      "file": "name",
      "line": 1,
      "type": "Error",
      "details": "text"
    }
  ]
}
"""


class Base64:
    CONTENT = ".base64"
    MESSAGE = "message.base64"
    PATCH = "patch.base64"


class Format:
    DETAILS = "details"
    FILE = "file"
    LINE = "line"
    TYPE = "type"


class Type:
    ERROR = "Error"
    INFO = "Info"
    WARN = "Warning"

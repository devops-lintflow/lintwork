# -*- coding: utf-8 -*-


"""
{
  "lint": [
    {
      "file": "name",
      "line": 1,
      "type": "Error",
      "details": "text"
    }
  ]
}
"""


class File:
    MESSAGE = "message"
    PATCH = "patch"


class Report:
    DETAILS = "details"
    FILE = "file"
    LINE = "line"
    TYPE = "type"


class Type:
    ERROR = "Error"
    INFO = "Info"
    WARN = "Warn"

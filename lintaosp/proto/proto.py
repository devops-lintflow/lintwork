# -*- coding: utf-8 -*-


"""Prototype
{
  "fileName": "/path/to/file",
  "lineNum": 1,
  "colNum": 1,
  "errorNum": "strings",
  "errorDetails": "details",
  "errorType": "E"
}
"""


class Format:
    COLNUM = "colnum"
    ERRORDETAILS = "errordetails"
    ERRORNUM = "errornum"
    ERRORTYPE = "errortype"
    FILENAME = "filename"
    LINENUM = "linenum"


class Type:
    ERROR = "E"
    INFO = "I"
    WARN = "W"

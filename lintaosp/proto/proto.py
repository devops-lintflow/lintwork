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


class ErrorFormat:
    COLNUM = "colnum"
    ERRORDETAILS = "errordetails"
    ERRORNUM = "errornum"
    ERRORTYPE = "errortype"
    FILENAME = "filename"
    LINENUM = "linenum"


class ErrorType:
    ERROR = "E"
    INFO = "I"
    WARN = "W"

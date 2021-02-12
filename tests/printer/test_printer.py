# -*- coding: utf-8 -*-

import os

from lintaosp.printer.printer import Printer, PrinterException
from lintaosp.proto.proto import ErrorFormat, ErrorType


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = {
        "strings": {
            ErrorFormat.FILENAME: "/path/to/file",
            ErrorFormat.LINENUM: 1,
            ErrorFormat.COLNUM: 1,
            ErrorFormat.ERRORNUM: "strings",
            ErrorFormat.ERRORDETAILS: "details",
            ErrorFormat.ERRORTYPE: ErrorType.ERROR,
        }
    }

    printer = Printer()

    name = "printer.json"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.txt"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.xlsx"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

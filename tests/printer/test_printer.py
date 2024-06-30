# -*- coding: utf-8 -*-

import os

from lintwork.format.format import Type
from lintwork.printer.printer import Printer, PrinterException


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    lint = "lintshell"

    reports = [
        {"file": "file1", "line": 1, "type": Type.ERROR, "details": "details1"},
        {"file": "file2", "line": 2, "type": Type.WARN, "details": "details2"},
    ]

    printer = Printer()

    name = "printer.json"
    printer.run(lint=lint, reports=reports, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.txt"
    printer.run(lint=lint, reports=reports, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.xlsx"
    printer.run(lint=lint, reports=reports, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

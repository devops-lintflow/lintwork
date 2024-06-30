# -*- coding: utf-8 -*-

import os

from lintwork.format.format import Type
from lintwork.printer.printer import Printer, PrinterException


class LintReport:
    file = ""
    line = ""
    type = ""
    details = ""


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    lint = "lintshell"

    report1 = LintReport()
    report1.file = "file1"
    report1.line = 1
    report1.type = Type.ERROR
    report1.details = "details1"

    report2 = LintReport()
    report2.file = "file2"
    report2.line = 2
    report2.type = Type.WARN
    report2.details = "details2"

    reports = [report1, report2]

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

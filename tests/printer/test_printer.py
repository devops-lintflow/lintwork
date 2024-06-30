# -*- coding: utf-8 -*-

import os

from lintwork.format.format import Report, Type
from lintwork.printer.printer import Printer, PrinterException


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = [
        {
            Report.FILE: "name1",
            Report.LINE: 1,
            Report.TYPE: Type.ERROR,
            Report.DETAILS: "text1",
        },
        {
            Report.FILE: "name2",
            Report.LINE: 2,
            Report.TYPE: Type.WARN,
            Report.DETAILS: "text2",
        },
    ]

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

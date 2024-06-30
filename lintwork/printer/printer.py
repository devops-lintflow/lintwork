# -*- coding: utf-8 -*-

import json
import openpyxl
import os
import time

from lintwork.format.format import Report


class PrinterException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Printer(object):
    _format = [".json", ".txt", ".xlsx"]

    def __init__(self, config=None):
        if config is None:
            pass

    @staticmethod
    def format():
        return Printer._format

    def _json(self, lint, reports, name):
        with open(name, "w", encoding="utf-8") as f:
            buf = []
            for item in reports:
                buf.append(
                    {
                        Report.FILE: item.file,
                        Report.LINE: item.line,
                        Report.TYPE: item.type,
                        Report.DETAILS: item.details,
                    }
                )
            json.dump({lint: buf}, f)

    def _txt(self, lint, reports, name):
        with open(name, "w", encoding="utf8") as f:
            for item in reports:
                f.write(
                    "%s:%s:%d:%s:%s"
                    % (lint, item.file, item.line, item.type, item.details)
                )
                f.write("\n")

    def _xlsx(self, lint, reports, name):
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
        ws = wb.create_sheet()
        ws.title = "%s" % time.strftime("%Y-%m-%d", time.localtime(time.time()))
        for item in reports:
            ws.append([lint, item.file, item.line, item.type, item.details])
        wb.save(filename=name)

    def run(self, lint, reports, name, append=True):
        if append is True:
            raise PrinterException("append not supported")
        func = Printer.__dict__.get(os.path.splitext(name)[1].replace(".", "_"), None)
        if func is not None:
            func(self, lint, reports, name)

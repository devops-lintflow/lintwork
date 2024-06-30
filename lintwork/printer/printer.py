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
            f.write(json.dumps({lint: reports}, ensure_ascii=False, indent=2))
            f.write("\n")

    def _txt(self, lint, reports, name):
        with open(name, "w", encoding="utf8") as f:
            for item in reports:
                f.write(
                    "%s:%s:%d:%s:%s"
                    % (
                        lint,
                        item[Report.FILE],
                        item[Report.LINE],
                        item[Report.TYPE],
                        item[Report.DETAILS],
                    )
                )
                f.write("\n")

    def _xlsx(self, lint, reports, name):
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
        ws = wb.create_sheet()
        ws.title = "%s" % time.strftime("%Y-%m-%d", time.localtime(time.time()))
        for item in reports:
            ws.append(
                [
                    lint,
                    item[Report.FILE],
                    item[Report.LINE],
                    item[Report.TYPE],
                    item[Report.DETAILS],
                ]
            )
        wb.save(filename=name)

    def run(self, lint, reports, name, append=True):
        if append is True:
            raise PrinterException("append not supported")
        func = Printer.__dict__.get(os.path.splitext(name)[1].replace(".", "_"), None)
        if func is not None:
            func(self, lint, reports, name)

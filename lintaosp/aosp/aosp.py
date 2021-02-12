# -*- coding: utf-8 -*-

from lintaosp.aosp.strings import Strings
from lintaosp.config.config import ConfigFile
from lintaosp.printer.printer import Printer


class AospException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Aosp(object):
    def __init__(self, config):
        if config is None:
            raise AospException("config invalid")
        self._config = config
        self._spec = config.config_file.get(ConfigFile.SPEC, None)
        if self._spec is None:
            raise AospException("spec invalid")

    def _dump(self, data):
        printer = Printer()
        printer.run(data=data, name=self._config.output_file, append=False)

    def _instance(self):
        buf = {}
        if Strings.__name__.lower() in self._spec:
            buf[Strings.__name__.lower()] = Strings(self._config)
        return buf

    def routine(self, data):
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise AospException("data invalid")
        buf = {}
        for key, val in self._instance().items():
            b = []
            for item in data:
                b.append(val.run(item))
            buf[key] = b
        if len(self._config.output_file) != 0:
            self._dump(buf)
        return buf

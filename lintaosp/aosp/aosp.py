# -*- coding: utf-8 -*-

from lintaosp.aosp.sdk import Sdk
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
        self._instance = self._instantiate()

    def _dump(self, data):
        printer = Printer()
        printer.run(data=data, name=self._config.output_file, append=False)

    def _instantiate(self):
        buf = {}
        if Sdk.__name__.lower() in self._spec:
            buf[Sdk.__name__.lower()] = Sdk(self._config)
        return buf

    def routine(self, data):
        if data is None or not isinstance(data, str) or len(data) == 0:
            raise AospException("data invalid")
        buf = {}
        for key in self._spec.keys():
            if key in self._instance.keys():
                buf[key] = self._instance[key].run(data)
        if len(self._config.output_file) != 0:
            self._dump(buf)
        return buf

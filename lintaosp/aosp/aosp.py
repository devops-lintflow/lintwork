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
        if Strings.__name__.lower() in self._spec.keys():
            buf[Strings.__name__.lower()] = Strings(self._config)
        return buf

    def routine(self, host=None, spec=None):
        hosts = []
        if host is not None and isinstance(host, str):
            hosts.append(host)
        else:
            hosts = self._instance().keys()
        specs = []
        if spec is not None and isinstance(spec, str):
            specs.append(spec)
        else:
            for item in hosts:
                buf = self._spec.get(item, [])
                if buf is not None and len(buf) > 0:
                    specs.extend(buf)
        buf = {}
        for h in hosts:
            b = {}
            for s in specs:
                b[s] = self._instance()[h].run(s)
                buf[h] = b
        if len(self._config.output_file) != 0:
            self._dump(buf)
        return buf

# -*- coding: utf-8 -*-

from lintaosp.aosp.abstract import AospAbstract


class SdkException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Sdk(AospAbstract):
    def __init__(self, config):
        super().__init__(config)

    def _execution(self, data):
        return "sdk"

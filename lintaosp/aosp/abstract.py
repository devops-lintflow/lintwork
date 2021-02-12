# -*- coding: utf-8 -*-

import abc


class AospAbstract(abc.ABC):
    def __init__(self, config):
        self._config = config

    @abc.abstractmethod
    def _execution(self, data):
        pass

    def run(self, data):
        return self._execution(data)

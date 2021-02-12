# -*- coding: utf-8 -*-

import argparse

from lintaosp.__version__ import __version__


class Argument(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="Lint AOSP")
        self._add()

    def _add(self):
        self._parser.add_argument(
            "--config-file",
            action="store",
            dest="config_file",
            help="config file (.yml)",
            required=True,
        )
        group = self._parser.add_mutually_exclusive_group()
        group.add_argument(
            "--input-text",
            action="store",
            default="",
            dest="input_text",
            help="input text (base64)",
            required=False,
        )
        group.add_argument(
            "--listen-url",
            action="store",
            default="",
            dest="listen_url",
            help="listen url (host:port)",
            required=False,
        )
        self._parser.add_argument(
            "--output-file",
            action="store",
            default="",
            dest="output_file",
            help="output file (.json|.txt|.xlsx)",
            required=False,
        )
        self._parser.add_argument(
            "-v", "--version", action="version", version=__version__
        )

    def parse(self, argv):
        return self._parser.parse_args(argv[1:])

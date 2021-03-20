# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config, ConfigException


def test_exception():
    exception = ConfigException("exception")
    assert str(exception) == "exception"


def test_config():
    config = Config()

    try:
        config.config_file = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = "config.json"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = "foo.yml"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = os.path.join(
            os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
        )
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.lint_project = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.lint_project = "/invalid/project"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.lint_project = os.path.join(
            os.path.dirname(__file__), "../data/java".replace("/", os.path.sep)
        )
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.listen_url = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.listen_url = "127.0.0.1:9090"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.output_file = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.output_file = ""
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.output_file = "output.foo"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.output_file = "output.json"
    except ConfigException as _:
        assert False
    else:
        assert True

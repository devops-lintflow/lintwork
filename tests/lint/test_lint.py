# -*- coding: utf-8 -*-

import os

from lintwork.config.config import Config
from lintwork.lint.lint import Lint, LintException, LintProto


class LintFile:
    path = ""
    content = ""


class LintMeta:
    path = ""
    content = ""


class LintPatch:
    path = ""
    content = ""


def test_exception():
    exception = LintException("exception")
    assert str(exception) == "exception"


def test_lint():
    try:
        _ = Lint(None)
    except LintException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Lint(config)
    except LintException as _:
        assert False
    else:
        assert True


def test_lintproto():
    proto = LintProto(None)

    file1 = LintFile()
    file1.path = "COMMIT_MSG"
    file1.content = "QWRkIHRlc3QgZmlsZXMgMTE6MTMNCg0KQ2hhbmdlLUlkOiBJZDAyMWI2NjU5YmViMTliODQ0MzcxOTFkMjk0YjcyZDljMjk0ZGYzYg=="

    file2 = LintFile()
    file2.path = "lintshell/test.sh"
    file2.content = "IyEvYmluL2Jhc2gNCg0KZWNobyAiSGVsbG8gU2hlbGwhIg0K"

    files = [file1, file2]

    meta = LintMeta()
    meta.path = "42-a4bc7bd.meta"
    meta.content = "ew0KICAidXJsIjogImh0dHA6Ly8xMjcuMC4wLjE6ODA4MCIsDQogICJwcm9qZWN0IjogImxpbnRzaGVsbCIsDQogICJicmFuY2giOiAibWFzdGVyIiwNCiAgIm93bmVyIjogIm5hbWUiLA0KICAicmV2aXNpb24iOiAiNTMzY2Y1Y2ZkZmUwNDdkMjY4OWUzM2M1ZTYyNDMyNWMzZDlmZmUzOCIsDQogICJ1cGRhdGVkIjogIjIwMjQtMDktMjAgMDc6MTU6NDQuNjM5MDAwMDAwIg0KfQ0K"

    patch = LintPatch()
    patch.path = "42-a4bc7bd.patch"
    patch.content = "RnJvbSA1MzNjZjVjZmRmZTA0N2QyNjg5ZTMzYzVlNjI0MzI1YzNkOWZmZTM4IE1vbiBTZXAgMTcgMDA6MDA6MDAgMjAwMQ0KRnJvbTogSmlhIEppYSA8YW5nZXJzYXhAc2luYS5jb20+DQpEYXRlOiBTdW4sIDMwIEp1biAyMDI0IDEwOjQyOjIwICswODAwDQpTdWJqZWN0OiBbUEFUQ0hdIEFkZCB0ZXN0IGZpbGVzIDExOjEzDQoNCkNoYW5nZS1JZDogSWQwMjFiNjY1OWJlYjE5Yjg0NDM3MTkxZDI5NGI3MmQ5YzI5NGRmM2INCi0tLQ0KDQpkaWZmIC0tZ2l0IGEvbGludHNoZWxsL3Rlc3Quc2ggYi9saW50c2hlbGwvdGVzdC5zaA0KbmV3IGZpbGUgbW9kZSAxMDA3NTUNCmluZGV4IDAwMDAwMDAuLmJiNTRmZTUNCi0tLSAvZGV2L251bGwNCisrKyBiL2xpbnRzaGVsbC90ZXN0LnNoDQpAQCAtMCwwICsxLDMgQEANCisjIS9iaW4vYmFzaA0KKw0KK2VjaG8gIkhlbGxvIFNoZWxsISINCg=="

    project = proto._build(files, meta, patch)
    if project is not None and os.path.exists(project):
        assert True

    proto._clean(project)

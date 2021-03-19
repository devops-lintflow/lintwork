# -*- coding: utf-8 -*-

from lintwork.work.linux.checkpatch import Checkpatch, CheckpatchException


def test_exception():
    exception = CheckpatchException("exception")
    assert str(exception) == "exception"


def test_checkpatch():
    with open("../../data/linux/checkpatch.txt", "r") as f:
        data = f.read()

    try:
        checkpatch = Checkpatch([])
        buf = checkpatch._parse(data)
    except CheckpatchException as _:
        assert False
    else:
        assert True

    assert len(buf) != 0

# -*- coding: utf-8 -*-

import queue

from lintwork.queue.queue import Queue, QueueException
from lintwork.queue.queue import Worker, WorkerException


def routine(_):
    pass


def test_queueexception():
    exception = QueueException("exception")
    assert str(exception) == "exception"


def test_queue():
    try:
        q = Queue(None)
    except QueueException as _:
        assert False
    else:
        assert True

    args = "args"

    try:
        q.run(routine, args)
    except QueueException as _:
        assert False
    else:
        assert True


def test_workerexception():
    exception = WorkerException("exception")
    assert str(exception) == "exception"


def test_worker():
    _queue = queue.Queue(1)
    _queue.put((routine, "args"))

    try:
        _ = Worker(_queue=_queue)
    except WorkerException as _:
        assert False
    else:
        assert True

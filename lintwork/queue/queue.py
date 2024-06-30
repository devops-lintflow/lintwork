# -*- coding: utf-8 -*-

import queue
import threading

QUEUE_NUM = 1
ROUTINE_NUM = 1


class QueueException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Queue(object):
    def __init__(self, config):
        if config is None:
            pass
        self._queue = queue.Queue(QUEUE_NUM)
        for _ in range(ROUTINE_NUM):
            Worker(self._queue)

    def _add(self, routine, lint, project):
        self._queue.put((routine, lint, project))

    def _wait(self):
        self._queue.join()

    def run(self, routine, lint, project):
        for _ in range(QUEUE_NUM):
            self._add(routine, lint, project)
        self._wait()


class WorkerException(QueueException):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Worker(threading.Thread):
    def __init__(self, _queue):
        super(Worker, self).__init__()
        self._queue = _queue
        self.daemon = True
        self.start()

    def run(self):
        while True:
            routine, lint, project = self._queue.get()
            routine(lint, project)
            self._queue.task_done()

#!/usr/bin/env python
# coding=utf-8
import time

event_list = []


class Event(object):

    def __init__(self, *args, **kwargs):
        self.callback = lambda: None
        event_list.append(self)

    def set_callback(self, callback):
        self.callback = callback

    def is_ready(self):
        result = self._is_ready()

        if result:
            self.callback()

        return result


class SleepEvent(Event):

    def __init__(self, timeout):
        super(SleepEvent, self).__init__(timeout)
        self.timeout = timeout
        self.start_time = time.time()

    def _is_ready(self):
        return time.time() - self.start_time >= self.timeout


def sleep(timeout):
    return SleepEvent(timeout)


def run(tasks):
    for task in tasks:
        _next(task)

    while len(event_list):
        for event in event_list:
            if event.is_ready():
                event_list.remove(event)
                break


def _next(task):
    try:
        event = next(task)
        event.set_callback(lambda: _next(task))
    except StopIteration:
        pass


def task_func(name):
    print name, 1
    yield sleep(1)
    print name, 2
    yield sleep(2)
    print name, 3


if __name__ == '__main__':
    run((task_func('tb'), task_func('py')))

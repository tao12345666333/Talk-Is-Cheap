#!/usr/bin/env python
# coding=utf-8
from collections import deque


class Runner(object):

    def __init__(self, task):
        self.task = deque(task)

    def next(self):
        return self.task.pop()

    def run(self):
        while len(self.task):
            task = self.next()
            try:
                next(task)
            except StopIteration:
                pass
            else:
                self.task.appendleft(task)


def task(name, times):

    for i in range(times):
        yield
        print name, i


if __name__ == "__main__":
    Runner([
        task('tb', 6),
        task('py', 3),
        task('cy', 3)
    ]).run()

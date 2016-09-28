#!/usr/bin/env python
# coding=utf-8
from tornado import ioloop, gen


@gen.coroutine
def task():

    for i in range(10):
        print i
        yield i


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    ioloop.run_sync(task)

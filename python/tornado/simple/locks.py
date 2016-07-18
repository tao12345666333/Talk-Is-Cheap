#!/usr/bin/env python
# coding=utf-8
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Condition

condition = Condition()

@gen.coroutine
def waiter():
    print 'wait here'
    yield condition.wait()
    print 'done waiting'


@gen.coroutine
def notifier():
    print 'ready notify'
    condition.notify()
    print 'done notify'


@gen.coroutine
def runner():
    yield [waiter(), notifier()]


if __name__ == '__main__':
    IOLoop.current().run_sync(runner)

#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
from tornado import gen
from tornado.concurrent import Future


@gen.coroutine
def asyn_connect(a, b):
    print 'ready to connect %s and %s' % (a, b)
    future = Future()

    def callback(a, b):
        print 'connect %s and %s' % (a, b)
        future.set_result(str(a) + str(b))

    tornado.ioloop.IOLoop.instance().add_callback(callback, a, b)

    result = yield future

    print 'after yielded'

    print 'the string %s and %s after connect is %s' % (a, b, result)


def main():
    asyn_connect('tao', 'beier')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# coding=utf-8
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=2)


@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print 'doing work on %s' % item
            yield gen.sleep(0.01)
        finally:
            q.task_done()


@gen.coroutine
def producer():
    for item in range(10):
        yield q.put(item)
        print 'put %s' % item


@gen.coroutine
def main():
    IOLoop.current().spawn_callback(consumer)
    yield producer()
    yield q.join()
    print 'done'


if __name__ == '__main__':
    IOLoop.current().run_sync(main)

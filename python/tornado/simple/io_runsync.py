#!/usr/bin/env python
# coding=utf-8
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=4)


@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print 'do %s' % item
            yield gen.sleep(5)

        finally:
            q.task_done()


@gen.coroutine
def producer():
    for item in range(15):
        yield q.put(item)
        print 'put %s' % item


@gen.coroutine
def main():
    IOLoop.current().spawn_callback(consumer)
    yield producer()
    yield q.join()

    print 'done'

if __name__ == '__main__':
    IOLoop().run_sync(main)

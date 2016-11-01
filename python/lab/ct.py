#!/usr/bin/env python
# coding=utf-8
import time
import threading
import tornado.ioloop
from tornado.concurrent import Future

ioloop = tornado.ioloop.IOLoop.current()


def long_task(future, sec=5):
    print("long task start")
    time.sleep(sec)
    print("after sleep")
    future.set_result("long task done in %s sec" % sec)


def after_task_done(future):
    print("task done")
    print(future.result())


def test_future():
    future = Future()
    threading.Thread(target=long_task, args=(future,)).start()
    ioloop.add_future(future, after_task_done)

if __name__ == "__main__":
    ioloop.add_callback(test_future)
    ioloop.start()

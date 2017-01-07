#!/usr/bin/env python
# coding=utf-8
import time
import threading
import random
import Queue


q = Queue.Queue()


def cp(n):
    return n * 2


def producer():
    while 1:
        wt = random.random()
        time.sleep(wt)
        q.put((cp, wt))


def consumer():
    while 1:
        task, arg = q.get()
        print arg, task(arg)
        q.task_done()


for target in (producer, consumer):
    t = threading.Thread(target=target)
    t.start()

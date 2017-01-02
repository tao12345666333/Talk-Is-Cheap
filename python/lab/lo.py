#!/usr/bin/env python
# coding=utf-8
import time
import threading


def consumenr(cond):
    t = threading.current_thread()
    with cond:
        cond.wait()
        print '{}: resource is available to consumenr'.format(t.name)


def producer(cond):
    t = threading.current_thread()
    with cond:
        print '{}: making resource available'.format(t.name)
        cond.notify_all()


condition = threading.Condition()


c1 = threading.Thread(name='c1', target=consumenr, args=(condition,))
c2 = threading.Thread(name='c2', target=consumenr, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))


c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()

#!/usr/bin/env python
# coding=utf-8
import time
from random import random
from threading import Semaphore, Thread, Timer


sem = Semaphore(5)


def foo(tid):
    with sem:
        print '{} acquire sem'.format(tid)
        wt = random() * 2
        time.sleep(wt)

    print '{} release sem'.format(tid)


def multit():
    threads = []

    for i in range(500):
        t = Thread(target=foo, args=(i,))
        # print t
        threads.append(t)
        t.start()
        # print t

    for t in threads:
        t.join()


def timer_test():
    print 'timer run'

if __name__ == '__main__':
    # multit()
    t = Timer(30.0, timer_test)
    t.start()

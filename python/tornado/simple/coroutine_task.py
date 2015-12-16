#!/usr/bin/env python
# coding=utf-8
import time

from concurrent.futures import ThreadPoolExecutor
from tornado import gen

executor = ThreadPoolExecutor(max_workers=2)


def cal(a, b):
    print 'run calculate %s + %s' % (a, b)
    print 'result is %s' % (a + b)
    time.sleep(10)


@gen.coroutine
def main(a, b):
    print 'ready to calculate %s + %s' % (a, b)
    yield executor.submit(cal, a, b)


if __name__ == '__main__':
    main(1, 2)

#!/usr/bin/env python
# coding=utf-8
import time
import multiprocessing

from threading import Thread


class Ct(Thread):
    def __init__(self, n):
        super(Ct, self).__init__()
        self.n = 0

    def run(self):
        while self.n > 0:
            print('n: {}'.format(self.n))
            self.n -= 1
            time.sleep(3)


if __name__ == '__main__':
    c = Ct(20)
    p = multiprocessing.Process(target=c.run)
    p.start()

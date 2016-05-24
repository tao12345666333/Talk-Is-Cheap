#!/usr/bin/env python
# coding=utf-8


def p():
    while True:
        string = yield
        print string


if __name__ == '__main__':
    pf = p()
    next(pf)
    pf.send('Hello')
    pf.send(' ')
    pf.send('World')
    pf.send('!')

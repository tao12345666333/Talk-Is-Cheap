#!/usr/bin/env python
# coding=utf-8
import string
from random import choice


def main():
    res = set()
    while len(res) <= 200:
        _d = ''.join(choice(string.ascii_uppercase + string.digits) for i in range(32))
        print _d
        res.add(_d)


if __name__ == '__main__':
    main()

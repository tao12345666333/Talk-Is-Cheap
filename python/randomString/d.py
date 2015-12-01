#!/usr/bin/env python
# coding=utf-8
from OpenSSL import rand
import base64


def main():
    res = set()
    while len(res) <= 200:
        _d = base64.urlsafe_b64encode(rand.bytes(20))
        print _d
        res.add(_d)


if __name__ == '__main__':
    main()

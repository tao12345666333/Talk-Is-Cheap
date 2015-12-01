#!/usr/bin/env python
# coding=utf-8
import uuid


def main():
    res = set()
    while len(res) <= 200:
        _d = str(uuid.uuid4()).replace('-', '')
        print _d
        res.add(_d)


if __name__ == '__main__':
    main()

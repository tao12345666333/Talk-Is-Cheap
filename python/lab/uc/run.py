#!/usr/bin/env python
# coding=utf-8

from ctypes import cdll


def main():
    so = cdll.LoadLibrary('fc.so')

    print so.add(9, 2)


if __name__ == '__main__':
    main()

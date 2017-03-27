#!/usr/bin/env python
# coding=utf-8

import random
import string


def main():
    print ''.join(random.sample(string.letters + string.digits, 16))


if __name__ == '__main__':
    main()

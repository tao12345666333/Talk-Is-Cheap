#!/usr/bin/env python
# coding=utf-8
"""Hello
"""
import sys
import json


def main():

    assert sys.argv[1] == 'update'

    print json.dumps({
        'name': 'moe',
        'sex': 0
    }, indent=4)


if __name__ == '__main__':
    main()

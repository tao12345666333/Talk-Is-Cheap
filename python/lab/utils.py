#!/usr/bin/env python
# coding=utf-8

import argparse


def main():
    parse = argparse.ArgumentParser(description='One util script')
    parse.add_argument('--action', '-a', type=str, required=True, help='action')
    parse.add_argument('--title', '-t', type=str, required=True, help='title')
    parse.add_argument('--url', '-u', type=str, required=True, help='url')

    args = parse.parse_args()

    print args.action, args.title, args.url


if __name__ == '__main__':
    main()

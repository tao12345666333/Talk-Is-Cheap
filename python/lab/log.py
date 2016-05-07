#!/usr/bin/env python
# coding=utf-8
import logging
from logging import NullHandler


def main():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, 'DEBUG'))
    logger.error('s')


if __name__ == '__main__':
    main()

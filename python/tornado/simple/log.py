#!/usr/bin/env python
# coding=utf-8
import logging
from tornado.log import enable_pretty_logging

logger = logging.getLogger()
enable_pretty_logging()
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    logger.info('info')
    logger.warning('Warning')
    logger.debug('DEBUG')
    logger.error('error')
    print('normal')

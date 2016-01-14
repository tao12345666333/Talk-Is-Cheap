#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import
import os
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def app_path_load(dir_level=2):
    app_root_path = os.path.abspath(__file__)
    for i in xrange(0, dir_level):
        app_root_path = os.path.dirname(app_root_path)

    sys.path.append(app_root_path)

app_path_load()

from task.celery import app


@app.task
def test_task(x, y):
    print x + y
    time.sleep(1)
    print 'finish'


def main():
    test_task.delay('a', 'b')

if __name__ == '__main__':
    main()

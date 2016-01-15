#!/usr/bin/env python
# coding=utf-8

import realpath
from task.celery import app


def add(a, b):
    print a + b



@app.task
def main():
    add(1, 5)


if __name__ == '__main__':
    main()

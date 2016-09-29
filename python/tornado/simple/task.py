#!/usr/bin/env python
# coding=utf-8

import pymongo
import redis

mc = pymongo.MongoClient()
r = redis.Redis()


class TaskManager():

    def __init__(self):
        pass

    def get_tasks(self):
        pass

    def save_task(self):
        pass


class RunTask():

    def __init__(self):
        pass

    def do(self):
        """run task
        """
        pass


if __name__ == '__main__':
    pass

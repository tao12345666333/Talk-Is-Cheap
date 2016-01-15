#!/usr/bin/python
# coding=utf-8
from __future__ import absolute_import

from celery import Celery
from celery.schedules import crontab

app = Celery(
    'task',
    backend='redis://127.0.0.1:6379/6',
    broker='redis://127.0.0.1:6379/7',
    include=['task.mytest']
)

app.conf.update(
    # CELERY_DEFAULT_QUEUE='default',
    # CELERY_QUEUES=(Queue('hipri'),),
    CELERYBEAT_SCHEDULE={
        "add": {
            "task": "task.mytest.main",
            "schedule": crontab('*/1'),
            "args": (),
            # "options": {'queue': 'hipri'}
            },
        },
)


if __name__ == '__main__':
    app.start()

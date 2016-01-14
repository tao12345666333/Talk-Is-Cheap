#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab

app = Celery('task', backend='redis://127.0.0.1:6379/0',
             broker='redis://127.0.0.1:6379/1',
             include=['task.mytask']
             )

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'add': {
            'task': 'task.mytask.main',
            'schedule': crontab(minute='*/1'),
            'args': (3, 3)
        }
    }
)


if __name__ == '__main__':
    app.start()

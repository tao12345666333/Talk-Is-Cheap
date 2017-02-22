#!/usr/bin/env python
# coding=utf-8

import requests
import time
import json

"""
ansible 运行结果回调

"""


class CallbackModule(object):

    # def __init__(self, *args, **kwargs):
        # pass

    def v2_runner_item_on_ok(self, *args, **kwargs):
        # time.sleep(10)
        # print args
        for i in dir(args[0]):
            if not i.startswith('__'):
                print i
        print '======'
        # print args[0]._result
        print json.dumps(args[0]._result, indent=4)
        print args[0]._task
        print 'runner item on ok'

    def v2_runner_item_on_failed(self, *args, **kwargs):
        # print args
        print dir(args[0])
        print 'runner item on failed'
        # print args[0]._result
        print json.dumps(args[0]._result, indent=4)
        print args[0]._task
        print '======'

    def v2_runner_item_on_skipped(self, *args, **kwargs):
        # print args
        print dir(args[0])
        print 'runner item on skipped'

    def v2_runner_retry(self, *args, **kwargs):
        # print args
        print dir(args[0])
        print 'runner on retry'

    def v2_runner_on_ok(self, *args, **kwargs):
        print 'runner on ok'
        # # print args
        # print dir(args[0])
        for i in dir(args[0]):
            if not i.startswith('__'):
                print i

        print '------'
        print json.dumps(args[0]._result, indent=4)
        print args[0]._task
        requests.post('http://127.0.0.1:9999/api/callback/test', args[0]._result)
        # print type(args[0]._task), 'task type'
        # print args[0]._host
        # print kwargs

    def v2_runner_on_unreachable(self, *args, **kwargs):
        print 'runner on unreacheable'
        # # print args
        print dir(args[0])
        # print args[0]._result
        # print args[0]._task
        # print args[0]._host
        # print kwargs

    def v2_runner_on_failed(self, *args, **kwargs):
        # # print args
        print dir(args[0])
        # print args[0]._result
        # print args[0]._task
        # print args[0]._host
        # print kwargs
        print 'runner on failed'
        print json.dumps(args[0]._result, indent=4)
        print args[0]._task

        requests.post('http://127.0.0.1:9999/api/callback/test', args[0]._result)
        requests.post('http://127.0.0.1:9999/api/callback/test', args[0]._task)
        print args[0].is_failed(),  '-*/***********'
        print '------'

    def v2_runner_on_skipped(self, *args, **kwargs):
        print 'runner on skipped'

    def v2_playbook_on_stats(self, *args, **kwargs):
        # print args
        # print dir(args[0])
        for i in dir(args[0]):
            if not i.startswith('__'):
                print i
        # print args[0].changed, 'changed'
        # print args[0].ok, 'ok'
        # print args[0].dark, 'dark'
        print args[0].failures, 'failures'

        # print args[0].increment, 'increment'
        # print args[0].processed, 'processed'
        # print args[0].skipped, 'skipped'
        # print args[0].summarize, 'summarize'
        # print kwargs
        print 'on stats'


if __name__ == '__main__':
    print 'callback'

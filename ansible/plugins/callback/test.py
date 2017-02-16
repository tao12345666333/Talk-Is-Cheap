#!/usr/bin/env python
# coding=utf-8

"""
ansible 运行结果
"""


class CallbackModule(object):

    def __init__(self, *args, **kwargs):
        print args
        print kwargs

    def v2_runner_on_ok(self, *args, **kwargs):
        print args
        print dir(args[0])
        print args[0]._result
        print args[0]._task
        print type(args[0]._task), 'task type'
        print args[0]._host
        print kwargs

    def v2_playbook_item_on_failed(self, *args, **kwargs):
        print args
        print dir(args[0])
        print args[0]._result
        print args[0]._task
        print args[0]._host
        print kwargs

    def v2_runner_on_unreachable(self, *args, **kwargs):
        print args
        print dir(args[0])
        print args[0]._result
        print args[0]._task
        print args[0]._host
        print kwargs

    def v2_runner_on_failed(self, *args, **kwargs):
        print args
        print dir(args[0])
        print args[0]._result
        print args[0]._task
        print args[0]._host
        print kwargs

    def v2_playbook_on_stats(self, *args, **kwargs):
        print args
        print dir(args[0])
        print args[0].changed, 'changed'
        print args[0].ok, 'ok'
        print args[0].dark, 'dark'
        print args[0].failures, 'failures'
        print args[0].increment, 'increment'
        print args[0].processed, 'processed'
        print args[0].skipped, 'skipped'
        print args[0].summarize, 'summarize'
        print kwargs


if __name__ == '__main__':
    print 'callback'

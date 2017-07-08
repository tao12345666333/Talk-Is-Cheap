#!/usr/bin/python
# coding=utf-8

"""
ansible callback plugin

所有用户存 Set
单个也存 Set
"""

from pymongo import MongoClient

mc = MongoClient()

host_db = mc['test']


class CallbackModule(object):
    """
    """

    def __init__(self):
        pass

    def v2_playbook_on_play_start(self, *args, **kwargs):
        pass

    def v2_runner_on_ok(self, res):
        if res._result.get('stdout_lines', None):
            # print res._result['stdout_lines']

            if host_db['host'].find_one({'host': str(res._host)}):
                host_db['host'].update({'host': str(res._host)},
                                       {'$set': {'users': res._result['stdout_lines']}})

            else:
                data = {
                    'host': str(res._host),
                    'users': res._result['stdout_lines']
                }

                host_db['host'].save(data)

                print data

    def v2_runner_on_failed(self, res, **kwargs):
        print 'failed: ',  res._host

    def v2_runner_on_unreachable(self, res):
        print 'unreacheable: ',  res._host

    def v2_runner_on_skipped(self, res):
        # data = {
            # 'status': 'skipped',
            # 'type': 'runner',
            # 'result': json.dumps(res._result),
            # 'name': str(res._task),
            # 'host': str(res._host),
        # }

        print 'skipped: ', res._host

    def v2_runner_item_on_ok(self, res):
        # print res._result['item']
        if res._result.get('stdout_lines', None):
            # print res._result['stdout_lines']
            if host_db['host'].find_one({'host': str(res._host)}):
                host_db['host'].update(
                    {'host': str(res._host)},
                    {'$set': {res._result['item']: res._result['stdout_lines'][0].split(',')}})

            else:
                data = {
                    'host': str(res._host),
                    res._result['item']: res._result['stdout_lines'][0].split(',')
                }

                host_db['host'].save(data)

                print data

    def v2_runner_item_on_failed(self, res):
        pass

    def v2_runner_item_on_skipped(self, res):
        pass

    def v2_runner_retry(self, res):
        pass

    def v2_playbook_on_stats(self, stats):
        """记录最终结果
        """
        # ips = {i for i in stats.ok.iterkeys()} | {i for i in stats.changed.iterkeys()}
        fail_ips = {i for i in stats.dark.iterkeys()} | {i for i in stats.failures.iterkeys()}

        print fail_ips


if __name__ == '__main__':
    print 'callback'

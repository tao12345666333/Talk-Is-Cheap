#!/usr/bin/env python
# coding=utf-8

from tornado import httpclient


def sync():
    client = httpclient.HTTPClient()

    try:
        res = client.fetch('http://httpbin.org/get')
        print res.body, 'sync'
    except httpclient.HTTPError as e:
        print('http error: ' + str(e))
    except Exception as e:
        print('error: ' + str(e))

    client.close()


def asyn():
    def handle_request(res):
        if res.error:
            print 'error: ', res.error
        else:
            print res.body

    client = httpclient.AsyncHTTPClient()
    client.fetch('http://httpbin.org/get', handle_request)


if __name__ == '__main__':
    sync()
    asyn()

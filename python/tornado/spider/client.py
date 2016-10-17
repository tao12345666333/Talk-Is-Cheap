#!/usr/bin/env python
# coding=utf-8


import tornado.httpclient


def block():
    http_client = tornado.httpclient.HTTPClient()
    try:
        res = http_client.fetch('http://httpbin.org/get')
        print res.body
    except tornado.httpclient.HTTPError as e:
        print('Error:' + e)
    except Exception as e:
        print('Error:' + e)

    http_client.close()


def no_block():
    def handle_request(res):
        if res.error:
            print('Error' + res.error)
        else:
            print(res.body)

    http_client = tornado.httpclient.AsyncHTTPClient()
    http_client.fetch('http://httpbin.org/get', handle_request)


if __name__ == '__main__':
    block()
    no_block()

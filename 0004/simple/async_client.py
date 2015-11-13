#!/usr/bin/env python
# coding=utf-8
from tornado.httpclient import AsyncHTTPClient


def asynchronous_fetch(url, callback):
    http_client = AsyncHTTPClient()

    def handle_res(res):
        callback(res.body)

    http_client.fetch(url, callback=handle_res)


if __name__ == '__main__':
    asynchronous_fetch('http://moelove.info', lambda x: x)

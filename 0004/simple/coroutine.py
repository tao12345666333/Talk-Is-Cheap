#!/usr/bin/env python
# coding=utf-8
from tornado.httpclient import AsyncHTTPClient
from tornado import gen


@gen.coroutine
def fetch_corotine(url):
    http_client = AsyncHTTPClient()
    res = yield http_client.fetch(url)
    raise gen.Return(res.body)


if __name__ == '__main__':
    fetch_corotine('https://google.com')

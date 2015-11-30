#!/usr/bin/env python
# coding=utf-8
from tornado.httpclient import AsyncHTTPClient
from tornado import gen


@gen.coroutine
def fetch_corotine(url):
    http_client = AsyncHTTPClient()
    res = yield http_client.fetch(url)
    raise gen.Return(res.body)


@gen.coroutine
def parallel_fetch(url1, url2):
    http_client = AsyncHTTPClient()
    resp1, resp2 = yield [http_client.fetch(url1),
                          http_client.fetch(url2)]


if __name__ == '__main__':
    # fetch_corotine('https://google.com')
    r = parallel_fetch('http://moelove.info', 'http://github.com')
    print type(r)

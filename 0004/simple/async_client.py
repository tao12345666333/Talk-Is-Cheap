#!/usr/bin/env python
# coding=utf-8
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future


def asynchronous_fetch(url, callback):
    http_client = AsyncHTTPClient()

    def handle_res(res):
        callback(res.body)

    http_client.fetch(url, callback=handle_res)


def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result())
    )

    return my_future

if __name__ == '__main__':
    # asynchronous_fetch('http://moelove.info', lambda x: x)
    async_fetch_future('http://google.com')

#!/usr/bin/env python
# coding=utf-8
from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    res = http_client.fetch(url)
    return res.body


if __name__ == '__main__':
    synchronous_fetch('http://google.com')

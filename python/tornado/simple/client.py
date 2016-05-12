#!/usr/bin/env python
# coding=utf-8
from tornado.httpclient import HTTPRequest


class RequestClient(HTTPRequest):
    SUPPORTED_METHODS = ("GET", "HEAD", "POST", "DELETE", "PATCH", "PUT",
                         "OPTIONS")

    def __init__(self, url, **kwargs):
        self.url = url

    def GET(self, **kwargs):
        pass

    def HEAD(self, **kwargs):
        pass

    def POST(self, **kwargs):
        pass

    def DELETE(self, **kwargs):
        pass

    def PATCH(self, **kwargs):
        pass

    def PUT(self, **kwargs):
        pass

    def OPTIONS(self, **kwargs):
        pass

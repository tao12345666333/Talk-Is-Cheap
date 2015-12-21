#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Main')
        self.write('the test url is %s' % self.reverse_url('test', 1))


class DictTestHandler(tornado.web.RequestHandler):

    def initialize(self, db):
        self.db = db

    def get(self, num):
        self.write('num is %s' % num)


if __name__ == '__main__':
    # 想要传递URLSpec的参数需要这样调用
    tornado.web.Application([
        tornado.web.url('/', MainHandler),
        tornado.web.url('/test/([0-9]+)', DictTestHandler, dict(db='db'),
                        name='test')
    ]).listen(9999)
    tornado.ioloop.IOLoop.current().start()

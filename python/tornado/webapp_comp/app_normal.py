#!/usr/bin/env python
# coding=utf-8

import time

import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import tornado.gen


define('port', default=8888, help='run server on the port', type=int)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Normal Handler')


class SleepHandler(tornado.web.RequestHandler):

    def get(self):
        time.sleep(10)
        self.write('Sleep Handler')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r'/main', MainHandler),
        (r'/sleep', SleepHandler),
    ])

    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

#!/usr/bin/env python
# coding=utf-8
import json
import time

import tornado.concurrent
import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


define("port", default=8000, help="run on the given port", type=int)


class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 5)
        self.write("when i sleep 5s")


class JustNowHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("i hope just now see you")


class TabHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(
            {
                'data': [
                    {
                        'name': 'tab1',
                        '_id': '5787a40fa901a81f3c052344',
                    },
                    {
                        'name': 'tab2',
                        '_id': '5787a40fa901a81f3c052345',
                    },
                    {
                        'name': 'tab3',
                        '_id': '5787a40fa901a81f3c052346',
                    },
                ],
                'count': 3,
                'code': 0,
            }
        ))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        'debug': True,
    }
    app = tornado.web.Application(handlers=[
        (r"/sleep", SleepHandler),
        (r"/justnow", JustNowHandler),
        (r"/api/tab", TabHandler),
    ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    # tornado.ioloop.IOLoop.instance().start()
    tornado.ioloop.IOLoop.current().start()

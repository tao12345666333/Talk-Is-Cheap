#!/usr/bin/env python
# coding=utf-8
"""
/ 提供基础页面
"""
import json
import time
import subprocess

import tornado.concurrent
import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.template
import pymongo
from tornado.options import define, options


mc = pymongo.MongoClient()
coll = mc['test']['conf']

define("port", default=9999, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html', data=coll.find())


class CreateHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('create.html')

    def post(self):
        ip = self.get_argument('ip')
        port = self.get_argument('port')
        print ip, port

        data = coll.insert_one({'ip': ip, 'port': port})

        conf = tornado.template.Template(
            """
            upstream app {
              server {{ ip }};
            }

            server {
              listen {{ port }};
              servername {{ ip }};
              charset  utf-8;
            }"""
        )

        print conf.generate(ip=ip, port=port)

        with open('confs/{}'.format(data.inserted_id), 'w+') as f:
            f.write(conf.generate(ip=ip, port=port))

        self.redirect('/')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", MainHandler),
        (r"/create", CreateHandler),
    ], template_path="template", debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    # tornado.ioloop.IOLoop.instance().start()
    tornado.ioloop.IOLoop.current().start()

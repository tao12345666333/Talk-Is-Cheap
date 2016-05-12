#!/usr/bin/env python
# coding=utf-8
import json

import requests
import tornado.concurrent
import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import xmltodict
from tornado.options import define, options


define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        # self.write("<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[签名失败]]></return_msg></xml>")
        self.write("<html><body><h1>T</h1></body></html>")

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # print self.request.body

        res = yield self.t_query()
        print res
        print type(res)
        self.write(str(res))

    @tornado.gen.coroutine
    def t_query(self):
        # res = requests.get('https://api.github.com/users/tao12345666333')

        def r(res):
            print res
            print '----'
            if res.error:
                return 'error %s' % res.error
            else:
                # return json.loads(res.content)
                # raise tornado.gen.Return(json.loads(res.body))
                self.write(res.body)
                # tornado.gen.Return(json.loads(res.body))

        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://ip.taobao.com/service/getIpInfo.php?ip=233.5.5.5', r)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        'debug': True
    }

    app = tornado.web.Application(handlers=[
        (r"/", MainHandler),
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

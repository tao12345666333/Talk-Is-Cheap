#!/usr/bin/env python
# coding=utf-8
import logging

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.escape
import tornado.locale
import tornado.websocket
import tornado.httpserver
import tornado.options

from tornado.options import define, options

options.logging = 'debug'
define("port", default=9999, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        # self.write(
            # '<html><body><form action="/form" method="POST">'
            # '<input type="text" name="msg">'
            # '<input type="text" name="msg">'
            # '<input type="submit" value="Submit">'
            # '</form></body></html>'
        # )
        self.write('get')

    def post(self):
        self.write(
            'The host is %s, method is %s, remote_ip is %s and UA is %s' % (
                self.request.host, self.request.method, self.request.remote_ip,
                self.request.headers.get('User-Agent')
            )
        )


class AsyncHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        res = yield http.fetch('http://apis.baidu.com/heweather/pro/attractions')
        json = tornado.escape.json_decode(res.body)
        self.write(json)

    @tornado.web.asynchronous
    def post(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://apis.baidu.com/heweather/pro/attractions', callback=self.on_response)

    def on_response(self, res):
        if res.error:
            raise tornado.web.HTTPError(500)

        json = tornado.escape.json_decode(res.body)
        self.write(json)
        self.finish()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    settings = {
        'debug': True,
        'compiled_template_cache': False
    }

    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/async', AsyncHandler),
    ], **settings)

    # app.listen(9999)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9999)
    logging.warning('start ..')
    tornado.ioloop.IOLoop.current().start()

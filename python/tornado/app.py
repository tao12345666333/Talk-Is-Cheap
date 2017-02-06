#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def inintialize(self):
        pass

    def prepare(self):
        pass

    def get(self):
        self.write('Hello world!')

    def on_finish(self):
        pass


class TestHandler(tornado.web.RequestHandler):

    def post(self):
        print self.request.uri
        with open('f.data', 'a+') as f:
            f.write('{}\n---\n'.format(self.request.body))

    def check_xsrf_cookie(self, *args, **kwargs):
        return True

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', MainHandler),
        ('/test', TestHandler),
    ])

    app.listen(9996,)

    tornado.ioloop.IOLoop().current().start()

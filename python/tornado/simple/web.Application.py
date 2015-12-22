#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Application')


if __name__ == '__main__':
    settings = {
        'debug': True
    }

    app = tornado.web.Application([
        ('/', MainHandler)
    ], **settings)

    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()

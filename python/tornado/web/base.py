#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop


class BaseHandler(tornado.web.RequestHandler):

    pass


class MainHandler(BaseHandler):

    def get(self):
        require = self.get_argument('param')
        option = self.get_argument('option', default='test')


if __name__ == '__main__':
    settings = {
        'debug': True
    }
    app = tornado.web.Application([
        ('/', MainHandler)
    ], **settings)

    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()

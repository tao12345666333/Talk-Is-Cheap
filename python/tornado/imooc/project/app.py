#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def initialize(self, url):
        print url
        print 'init'

    def prepare(self):
        print 'prepare'

    def get(self):
        print 'get handler'
        # self.write('Hello Tornado!')
        name = 'Tornado'
        self.render('index.html', name=name)

    def on_finish(self):
        print 'on_finish'


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', MainHandler, {'url': 'test'}),
    ])

    app.listen(9999)

    tornado.ioloop.IOLoop().current().start()

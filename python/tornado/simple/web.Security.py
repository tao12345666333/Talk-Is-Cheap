#!/usr/bin/env python
# coding=utf-8
import logging

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.ioloop
import tornado.locale
import tornado.web


class WebHandler(tornado.web.RequestHandler):

    def get(self):
        if not self.get_cookie('mycookie'):
            self.set_cookie('mycookie', 'mycookievalue')
            self.write('cookie not set yet')
        else:
            self.write('cookie set')


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        if not self.get_secure_cookie('mycookie'):
            self.set_secure_cookie('mycookie', 'mycookievalue', expires_days=2)
            self.write('cookie_secret not set yet')
        else:
            self.write('cookie_secret set')


if __name__ == '__main__':
    settings = {
        'debug': True,
        'compiled_template_cache': False,
        # 'cookie_secret': 'test_cookie'
        'cookie_secret': {
            1: 'test',
            2: 'my'
        },
        'key_version': 1
    }

    app = tornado.web.Application([
        (r'/', WebHandler),
        (r'/main', MainHandler)
    ], **settings)

    app.listen(9999)
    logging.warning('start ..')
    tornado.ioloop.IOLoop.current().start()

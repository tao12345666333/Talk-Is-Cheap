#!/usr/bin/env python
# coding=utf-8
import logging

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.ioloop
import tornado.locale
import tornado.web

import uimodules


ENTRIES = [
    {
        'name': 'one',
        'per': 'm'
    },
    {
        'name': 'two',
        'per': 'm'
    },
    {
        'name': 'three',
        'per': 'o'
    },
]


class PageHandler(tornado.web.RequestHandler):

    def get(self):
        logging.warning(self.request.path)
        logging.warning(tornado.locale.get_supported_locales())
        logging.warning(self.locale.name)

        self.render('template.html', title='test', items=map(str, range(10)))


class WebUIHandler(tornado.web.RequestHandler):

    def get(self):
        entries = ENTRIES
        self.render('home.html', entries=entries)


class WebHandler(tornado.web.RequestHandler):

    def get(self):
        entry = filter(lambda x: x['per'] is 'm', ENTRIES)[0]
        self.render('entry.html', entry=entry)


if __name__ == '__main__':
    settings = {
        'debug': True,
        'compiled_template_cache': False,
        'ui_modules': uimodules
    }

    app = tornado.web.Application([
        (r'/page', PageHandler),
        (r'/ui', WebUIHandler),
        (r'/web', WebHandler)
    ], **settings)

    app.listen(9999)
    logging.warning('start ..')
    tornado.ioloop.IOLoop.current().start()

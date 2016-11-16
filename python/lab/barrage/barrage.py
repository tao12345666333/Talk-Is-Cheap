#!/usr/bin/env python
# coding=utf-8

import os

import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.escape

import uuid

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html", messages=ChatHandler.cache)


class ChatHandler(tornado.websocket.WebSocketHandler):

    cache = []
    cache_size = 100
    users = set()

    def open(self):
        ChatHandler.users.add(self)

    def on_close(self):
        ChatHandler.users.remove(self)

    def on_message(self, message):
        msg = tornado.escape.json_decode(message)

        chat = {
            'id': str(uuid.uuid4()),
            'body': msg['body']
        }
        chat['html'] = tornado.escape.to_basestring(
            self.render_string('message.html', message=chat))

        self.cache.append(chat)

        for u in self.users:
            try:
                u.write_message(chat)
            except:
                print 'Error'


if __name__ == '__main__':
    settings = {
        'debug': True,
        'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),

        'xsrf_cookies': True,
        'cookie_secret': 'StuQ',
    }
    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/chatsocket', ChatHandler),
    ], **settings)

    app.listen(9966)
    tornado.ioloop.IOLoop.current().start()

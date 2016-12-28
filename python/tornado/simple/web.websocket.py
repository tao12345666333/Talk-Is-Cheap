#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.ioloop
import tornado.websocket


class MainHandler(tornado.websocket.WebSocketHandler):

    def check_origin(*args, **kwargs):
        """for deploy it with nginx reverse proxy
        Since Tornado 4.0, it has some changes.
        """
        return True

    def open(self):
        print('websocket open')

    def on_message(self, message):
        self.write_message('message is %s' % message)

    def on_close(self):
        print('websocket close')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),
    ])
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()

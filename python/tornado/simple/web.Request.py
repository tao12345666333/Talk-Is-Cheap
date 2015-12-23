#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('get')

    def post(self):
        self.write(
            'The host is %s, method is %s, remote_ip is %s and UA is %s' % (
                self.request.host, self.request.method, self.request.remote_ip,
                self.request.headers.get('User-Agent')
            )
        )


if __name__ == '__main__':
    settings = {
        'debug': True
    }

    app = tornado.web.Application([
        ('/', MainHandler)
    ], **settings)

    app.listen(9999)
    print 'start ..'
    tornado.ioloop.IOLoop.current().start()

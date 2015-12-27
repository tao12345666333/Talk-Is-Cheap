#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(
            '<html><body><form action="/form" method="POST">'
            '<input type="text" name="msg">'
            '<input type="text" name="msg">'
            '<input type="submit" value="Submit">'
            '</form></body></html>'
        )

    def post(self):
        self.write(
            'The host is %s, method is %s, remote_ip is %s and UA is %s' % (
                self.request.host, self.request.method, self.request.remote_ip,
                self.request.headers.get('User-Agent')
            )
        )


class FormHandler(tornado.web.RequestHandler):

    def post(self):
        self.set_header('Content-Type', 'text/plain')
        msg = self.get_arguments('msg')
        for i in msg:
            self.write('msg is %s\n' % i)


if __name__ == '__main__':
    settings = {
        'debug': True
    }

    app = tornado.web.Application([
        ('/', MainHandler),
        ('/form', FormHandler)
    ], **settings)

    app.listen(9999)
    print 'start ..'
    tornado.ioloop.IOLoop.current().start()

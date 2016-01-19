#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.escape
import tornado.httpserver


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie('user')


class MainHandler(BaseHandler):

    def get(self):
        if not self.get_current_user():
            print 'not user'
            self.redirect('/login')
            return

        name = tornado.escape.xhtml_escape(self.current_user)
        self.write('current_user is ' + name)


class LoginHandler(BaseHandler):

    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie('user', self.get_argument('name'))
        self.redirect('/')


if __name__ == '__main__':
    settings = {
        'debug': True,
        'cookie_secret': 'test0118'
    }

    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/login', LoginHandler)
    ], **settings)

    server = tornado.httpserver.HTTPServer(app)

    server.bind(9999)
    server.start(1)

    # app.listen(9999)
    print 'start..'

    tornado.ioloop.IOLoop.current().start()

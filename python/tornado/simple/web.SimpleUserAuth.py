#!/usr/bin/env python
# coding=utf-8
import tornado.web
import tornado.ioloop


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie('user')


class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("The current user is " + name)

    @tornado.web.authenticated
    def post(self):
        print self.current_user


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
    config = {
        'debug': True,
        'cookie_secret': 'testcookie',
        'login_url': '/login',
        # 'xsrf_cookies': True
    }

    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/login', LoginHandler)
    ], **config)

    app.listen(9999)
    print 'start ...'

    tornado.ioloop.IOLoop.current().start()

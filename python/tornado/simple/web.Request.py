#!/usr/bin/env python
# coding=utf-8
import logging
import os
import uuid

import tornado.ioloop
import tornado.web


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


class FileFormHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(
            '<html><body><form enctype="multipart/form-data" action="/file" method="POST">'
            '<input type="file" name="file">'
            '<input type="submit" value="Submit">'
            '</form></body></html>'
        )

    def post(self):
        fileinfo = self.request.files['file'][0]
        fname = fileinfo['filename']
        ctype = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + ctype

        f = open('./' + cname, 'w')
        f.write(fileinfo['body'])
        self.finish('%s is uploaded! and rename %s, check current folder.'
                    % (fname, cname))


class BaseHandler(tornado.web.RequestHandler):

    def get(self):
        pass

    def post(self):
        pass


if __name__ == '__main__':
    settings = {
        'debug': True
    }

    app = tornado.web.Application([
        ('/', MainHandler),
        ('/form', FormHandler),
        ('/file', FileFormHandler),
        ('/sequence', BaseHandler)
    ], **settings)

    app.listen(9999)
    logging.info('start ..')
    logging.warning('start ..')
    logging.debug('start debug')
    tornado.ioloop.IOLoop.current().start()

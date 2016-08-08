#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import re

import tornado.httpserver
import tornado.options
import tornado.web
from tornado.options import define, options

import requests

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("""
           <html>
             <head>
               <title>Redis</title>
             </head>
             <body>
               <form action="/" method="POST">
                 <div>
                   <label>key: </label>
                   <input type="text" name="key">
                 </div>
                 <div>
                   <label>url: </label>
                   <input type="text" name="url">
                 </div>
                 <div>
                   <input type="submit">
                 </div>
               </form>
             </body>
           </html>
        """)

    def post(self):
        key = self.get_argument('key')
        url = self.get_argument('url')

        if key != 'rz':
            self.redirect('/?status=fail')
            return

        if not url.startswith('http'):
            self.redirect('/?status=fail')
            return

        res = requests.get(url, verify=False)
        if res.status_code != 200:
            self.redirect('/?status=fail')
            return

        title = re.findall(r'<title>(.*?)</title>', res.content)[0]
        print 'title is: %s' % title.decode('utf-8')

        title = unicode(title, 'utf8')

        if not title:
            self.redirect('/?status=fail')
            return

        with open('Readme.md', 'a+') as f:
            f.write('* [{0}]({1})\n\n'.format(title, url))

        self.redirect('/?status=success')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

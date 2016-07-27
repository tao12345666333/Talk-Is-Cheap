#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.options
import tornado.web
from tornado.options import define, options


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
            return

        if not url.startswith('http'):
            return

        self.redirect('/?status=success')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

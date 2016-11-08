# -*- coding:utf-8 -*-
from turbo import register

import app
import api


register.register_group_urls('', [
    ('/', app.HomeHandler),
    ('/index', app.HomeHandler),
    ('/create/(dc)', app.CreateHandler),
    ('/list/(dc)', app.ListHandler),
    ('/edit/(dc)/([0-9a-f]{24})', app.EditHandler),
    ('/delete/(dc)/([0-9a-f]{24})', app.DelHandler),
])

register.register_group_urls('/v1', [
    ('', api.HomeHandler),
])

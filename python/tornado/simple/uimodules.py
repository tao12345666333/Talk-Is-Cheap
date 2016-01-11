#!/usr/bin/env python
# coding=utf-8

import tornado.web


class Entry(tornado.web.UIModule):

    def render(self, entry, show_comments=False):
        print 'entry render'
        return self.render_string('module-entry.html', entry=entry,
                                  show_comments=show_comments)

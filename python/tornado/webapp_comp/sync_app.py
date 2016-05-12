#!/usr/bin/env python
# coding=utf-8

import tornado.concurrent
import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


@tornado.gen.coroutine
def main():
    print 's'

    def r(res):
        print res
        print '----'
        if res.error:
            return 'error %s' % res.error
        else:
            print res.body

    http = tornado.httpclient.AsyncHTTPClient()
    print 's1'
    yield http.fetch('http://ip.taobao.com/service/getIpInfo.php?ip=233.5.5.5', r)
    print 's2'


if __name__ == "__main__":
    res = tornado.ioloop.IOLoop.current().run_sync(main)
    print res

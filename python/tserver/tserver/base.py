#!/usr/bin/env python
# coding=utf-8
"""Base handler"""
import SocketServer


class BaseHandler(SocketServer.BaseRequestHandler):
    """Hand all requests."""

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 9988
    server = SocketServer.TCPServer((HOST, PORT), BaseHandler)
    server.serve_forever()

#!/usr/bin/env python
# coding=utf-8
import unittest
from httputil import parse_request_start_line


class ParseRequestStartLineTest(unittest.TestCase):
    METHOD = "GET"
    PATH = "/foo"
    VERSION = "HTTP/1.1"

    def test_parse_request_start_line(self):
        start_line = " ".join([self.METHOD, self.PATH, self.VERSION])
        parsed_start_line = parse_request_start_line(start_line)
        self.assertEqual(parsed_start_line.method, self.METHOD)
        self.assertEqual(parsed_start_line.path, self.PATH)
        self.assertEqual(parsed_start_line.version, self.VERSION)
        print('use')

#!/usr/bin/env python
# coding=utf-8
"""Code from Tornado
https://github.com/tornadoweb/tornado/blob/master/tornado/httputil.py#L887-L910
"""

import collections
import re

RequestStartLine = collections.namedtuple(
    "RequestStartLine", ["method", "path", "version"]
)


def parse_request_start_line(line: str) -> RequestStartLine:
    try:
        method, path, version = line.split(" ")
    except ValueError:
        raise HTTPInputError("Malformed HTTP request line")
    if not re.match(r"^HTTP/1\.[0-9]$", version):
        raise HTTPInputError(
            "Malformed HTTP version in HTTP Request-Line: %r" % version
        )
    return RequestStartLine(method, path, version)


class HTTPInputError(Exception):
    pass


if __name__ == "__main__":
    print(parse_request_start_line("GET /foo HTTP/1.1"))

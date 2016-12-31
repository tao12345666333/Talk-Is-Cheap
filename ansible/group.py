#!/usr/bin/env python
# coding=utf-8
import json

data = {
    'g1': {
        'hosts': [
            '172.18.6.93',
            '172.18.6.176'
        ]
    }
}

print json.dumps(data)

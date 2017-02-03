#!/usr/bin/env python
# coding=utf-8
import json
import sys

data = {
    'g1': {
        'hosts': [
            '172.18.6.93',
            '172.18.6.176'
        ]
    }
}

with open('w.log', 'w') as f:
    f.write(str(sys.argv))


print json.dumps(data)

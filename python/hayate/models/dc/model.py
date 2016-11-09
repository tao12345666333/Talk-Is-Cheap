# -*- coding:utf-8 -*-

from base import *


class Dc(Model):
    """
    model for digital certificate

    field:

        name       名称
        desc       描述
        expiration 过期时间
        used       被绑定的项目
        spec       规则

        atime      创建时间
    """
    name = 'dc'

    field = {
        'name':            (basestring, ''),
        'desc':            (basestring, ''),

        'used':            (list, []),
        'spec':            (basestring, ''),

        'file':            (ObjectId, ''),
        'file_name':       (basestring, ''),

        'expiration':      (datetime, None),
        'atime':           (datetime, None),
    }

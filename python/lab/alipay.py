#!/usr/bin/env python
# coding=utf-8
from hashlib import md5
from urllib import urlencode

import requests


def encode_dict(params):
    for k, v in params.iteritems():
        params[k] = v.encode('utf-8')

    return params


class Alipay(object):

    GATEWAY = 'https://mapi.alipay.com/gateway.do'
    NOTIFY_GATEWAY_URL = 'https://mapi.alipay.com/gateway.do'\
        '?service=notify_verify&partner=%s&notify_id=%s'

    sign_key = None
    sign_tuple = ('sign_type', 'MD5', 'MD5')

    def __init__(self, pid, key, seller_id=None, seller_email=None):
        self.pid = pid
        self.key = key
        self.default_params = {
            '_input_charset': 'utf-8',
            'payment_type': '1',  # 默认为'1'->str '商品购买'
            'partner': pid
        }

        if seller_id:
            self.default_params['seller_id'] = seller_id
        elif seller_email:
            self.default_params['seller_email'] = seller_email
        else:
            raise Exception('need seller_id or seller_email')

    def generate_md5_sign(self, params):
        src = '&'.join(['%s=%s' % (key, value) for key,
                        value in sorted(params.items())]) + self.key
        return md5(src.encode('utf-8')).hexdigest()

    def _check_params(self, params, names):
        if not all(k in params for k in names):
            raise Exception('missing parameters')

    def _build_url(self, service, paramnames=None, **kwargs):
        """创建带签名的请求地址，paramnames为需要包含的参数名，用于避免出现过多的参数，默认使用全部参数
        """
        params = self.default_params.copy()
        params['service'] = service
        params.update(kwargs)
        if paramnames:
            params = dict([(k, params[k]) for k in paramnames if k in params])
        signkey, signvalue, signdescription = self.sign_tuple
        signmethod = getattr(
            self,
            'generate_%s_sign' % signdescription.lower(),
            None  # getattr raise AttributeError if not default provided
        )
        if signmethod is None:
            raise Exception(
                "This type '%s' of sign is not implemented yet."
                % signdescription)
        if self.sign_key:
            params.update({signkey: signvalue})
        params.update({signkey: signvalue,
                       'sign': signmethod(params)})

        # return '%s?%s' % (self.GATEWAY, urlencode(encode_dict(params)))
        return urlencode(encode_dict(params))

    def create_direct_pay_by_user_url(self, **kwargs):
        """手机即时到帐接口
        """
        self._check_params(kwargs, ('out_trade_no', 'subject'))

        if not kwargs.get('total_fee') and \
           not (kwargs.get('price') and kwargs.get('quantity')):
            raise Exception('total_fee or (price && quantiry) must have one.')

        url = self._build_url('mobile.securitypay.pay', **kwargs)
        return url

    def get_sign_method(self, **kwargs):
        signkey, signvalue, signdescription = self.sign_tuple
        signmethod = getattr(
            self,
            'generate_%s_sign' % signdescription.lower(),
            None
        )
        if signmethod is None:
            raise Exception("This type '%s' of sign is not implemented yet."
                            % signdescription)
        return signmethod

    def verify_notify(self, **kwargs):
        sign = kwargs.pop('sign', '')
        kwargs.pop('sign_type', '')
        signmethod = self.get_sign_method(**kwargs)
        if signmethod(kwargs) == sign:
            return self.check_notify_remotely(**kwargs)
        else:
            return False

    def check_notify_remotely(self, **kwargs):
        remote_result = requests.get(
            self.NOTIFY_GATEWAY_URL % (self.pid, kwargs['notify_id']),
            headers={'connection': 'close'},
            verify=False  # 取消ssl验证, 可能会有安全问题.
        ).text
        return remote_result == 'true'

    def single_trade_query(self, **kwargs):
        """
        单笔交易查询,返回xml.
        out_trade_no或者trade_no参数必须有一个.
        """
        if 'trade_no' not in kwargs and 'out_trade_no' not in kwargs:
            raise Exception('missing parameters')
        url = self._build_url('single_trade_query', paramnames=['service', 'partner', '_input_charset', 'sign', 'sign_type', 'trade_no', 'out_trade_no'], **kwargs)
        remote_result = requests.get(url, headers={'connection': 'close'}).text
        return remote_result

#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals

import logging
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr

logger = logging.getLogger("root")


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_mail(receive_addrs, msg_type=None, ssl_type=False, **kwargs):
    u"""Send email function

    :arg list receive_addrs: 收件人列表

    :arg str msg_type: 消息类型
         options:
             test: Test

    :arg bool ssl_type: 发送邮件时是否使用SSl来连接服务器, 有时会出现连接超时的情况

    """
    sender_addr = 'TaoBeier@moelove.info'
    sender_passwd = 'rN6vli2tEm8ULu'
    server = smtplib.SMTP(host="smtp.exmail.qq.com", port=465 if ssl_type else 25)

    try:
        server.login(sender_addr, sender_passwd)
        server.set_debuglevel(1)
        server.sendmail(sender_addr, receive_addrs, format_msg(sender_addr, receive_addrs, msg_type, **kwargs))
    except Exception, e:
        print e
        logger.error(str(e))


def format_msg(sender_addr, receive_addrs, msg_type, **kwargs):
    """format msg function
    """
    if msg_type == 'test':
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header('来自 {c} 的邮件'.format(**kwargs), 'utf-8').encode()
        html = MIMEText('亲爱的: <br/> 这里有个代码： <b>{code}</b> <br/><br/><img src="cid:img1"><br/><br/><span style="color:red;">详情地址</span>：<a href="{url}"> {url} </a>'.format(**kwargs), 'html', 'utf-8')
        msg.attach(html)

        fimg1 = open('img1.jpg', 'rb')
        img1 = MIMEImage(fimg1.read())
        fimg1.close()
        img1.add_header('Content-ID', '<img1>')
        msg.attach(img1)
    else:
        raise Exception

    msg['From'] = _format_addr(u'MoeLove <%s>' % sender_addr)
    msg['To'] = ','.join(receive_addrs)

    return msg.as_string()


if __name__ == '__main__':
    send_mail(['test@loli.com'], 'test',  code="code", url="http://moelove.info", c="MoeLove")

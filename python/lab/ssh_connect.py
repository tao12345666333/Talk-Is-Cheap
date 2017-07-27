#!/usr/bin/env python
# coding=utf-8
# Author: TaoBeier
import paramiko
import getpass


class SSHClient(object):

    def __init__(self, ip, port=22, username=None, pkey_path=None):

        try:
            self.pkey = paramiko.RSAKey.from_private_key_file(pkey_path)
        except paramiko.PasswordRequiredException:
            password = getpass.getpass('please input RSA key password: ')
            self.pkey = paramiko.RSAKey.from_private_key(pkey_path, password)

        self.ip = ip
        self.port = port
        self.username = username

    def connect(self):
        """The real connect
        """
        sc = paramiko.SSHClient()
        sc.load_system_host_keys()
        sc.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            sc.connect(hostname=self.ip, port=self.port,
                       username=self.username, pkey=self.pkey, timeout=20)
            return (True, sc)
        except Exception as e:
            print e
            return (False, e)


if __name__ == '__main__':

    flag, res = SSHClient(
        '', port=22, username='tao', pkey_path='/home/tao/.ssh/id_rsa').connect()

    if flag:
        print('connect ...')
    else:
        print('connect error')
        return

    _, stdout, stderr = res.exec_command(
        'ls')

    if stdout.channel.recv_exit_status() == 0:
        print('command run ')
    else:
        err_msg = stderr.read()
        print(err_msg)

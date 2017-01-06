#!/usr/bin/env python
# coding=utf-8
import json
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
loader = DataLoader()                     # 用来加载解析yaml文件或JSON内容,并且支持vault的解密
# 管理变量的类,包括主机,组,扩展等变量,之前版本是在 inventory 中的
variable_manager = VariableManager()
inventory = Inventory(loader=loader, variable_manager=variable_manager)
variable_manager.set_inventory(inventory)  # 根据 inventory 加载对应变量


class Options(object):
    '''
    这是一个公共的类,因为ad-hoc和playbook都需要一个options参数
    并且所需要拥有不同的属性,但是大部分属性都可以返回None或False
    因此用这样的一个类来省去初始化大一堆的空值的属性
    '''

    def __init__(self):
        self.connection = "local"
        self.forks = 1
        self.check = False

    def __getattr__(self, name):
        return None
options = Options()


def run_playbook():
    playbooks = ['task.yaml']  # 这里是一个列表, 因此可以运行多个playbook
    variable_manager.extra_vars = {
        "ansible_ssh_user": "root", "ansible_ssh_pass": "xxx"}  # 增加外部变量
    pb = PlaybookExecutor(playbooks=playbooks, inventory=inventory,
                          variable_manager=variable_manager, loader=loader, options=options, passwords=None)
    result = pb.run()
    print result
if __name__ == '__main__':
    run_playbook()

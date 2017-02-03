#!/bin/bash
# author: TaoBeier

if [[ $1 != "--list" ]]; then exit 1; fi
#task_extra_var=`ps -f --pid $PPID | grep ansible-playbook | grep -oh "task=\w*" | tail -1 | cut -f2 -d=`
task_extra_var=`ps -f -p $PPID | grep ansible-playbook | grep -oh "task=\w*" | tail -1 | cut -f2 -d=`
./group.py --task $task_extra_var

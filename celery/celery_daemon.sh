#!/bin/bash

usage="Usage: $0 [start | stop | restart]"

case $1 in
    (start)
        celery multi start worker -A task -B --logfile='task/task.log' --pidfile='task/task.pid'
        ;;
    (stop)
        celery multi stop worker -A task -B --logfile='task/task.log' --pidfile='task/task.pid'
        ;;

    (restart)
        celery multi restart worker -A task -B --logfile='task/task.log' --pidfile='task/task.pid'
        ;;

    (test)
        celery worker -A task -B --logfile='task/task.log' --pidfile='task/task.pid'
        ;;

    (*)
        echo $usage
        exit 1
        ;;

esac

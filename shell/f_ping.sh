#!/bin/bash
# ping all ips

for ip in 192.168.0.{0..50} ;
do
    (
        ping $ip -c2 &> /dev/null;

        if [ $? -eq 0 ];
        then
            echo $ip is alive
        fi
    )&
done
wait

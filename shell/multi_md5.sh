#!/bin/bash
PIDARRAY=()
for i in `find . -type f`:
do
    md5sum $i &
    PIDARRAY+=("$!")
done
wait ${PIDARRAY[@]}

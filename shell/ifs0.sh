#!/bin/bash
line="mongodb:x:121:65534::/home/mongodb:/bin/false"

oldIFS=$IFS
IFS=":"
count=0
for i in $line;
do
    [ $count -eq 0 ] && user=$i;
    [ $count -eq 6 ] && shell=$i;
    let count++;
done
IFS=$oldIFS

echo $user\'s shell is $shell;


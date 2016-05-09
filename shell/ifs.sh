#!/bin/bash
data='a,b,d,f,e,c m,n,o,p'

oldIFS=$IFS
IFS=,
for i in $data;
do
    echo I: $i
done
IFS=$oldIFS

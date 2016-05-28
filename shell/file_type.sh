#!/bin/bash
# 文件类型统计信息

if [ $# -ne 1 ];
then
    echo "$0 need a path for usage"
    exit
fi
path=$1

declare -A statarray;

while read line;
do
    ftype=`file -b "$line" | cut -d, -f1`
    let statarray["$ftype"]++;

done < <(find $path -type f -print)

echo ======Count============

for ftype in "${!statarray[@]}";
do
    echo $ftype: ${statarray["$ftype"]}
done

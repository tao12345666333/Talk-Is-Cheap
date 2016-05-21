#!/bin/bash
# 删除重复文件，只保留一份

ls -lS --time-style=long-iso | awk 'BEGIN {
    getline; getline;
    name1=$8; size=$5
}
{
    name2=$8;
    if (size==$5)
    {
        "md5sum "name1 | getline; csum1=$1;
        "md5sum "name2 | getline; csum2=$1;
        if ( csum1=csum2 )
        {
            print name1; print name2
        }
    };
    size=$5; name1=name2;
}' | sort -u > duplicates_files

cat duplicates_files | xargs -I {} md5sum {} | sort | uniq -w 32 | awk '{ print "^"$2"$" }' | sort -u > duplicates_xx

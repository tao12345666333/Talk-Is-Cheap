#!/bin/bash
sort -C $1;

if [ $? -eq 0 ];
then
    echo Sorted;
else
    echo Unsorted;
fi

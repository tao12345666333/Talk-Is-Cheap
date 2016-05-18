#!/bin/bash
for i in `find -name "*.sh"`;
do
    echo ${i%.*};
done

#!/bin/bash
# rename all picture files
count=0;
for i in `find . -maxdepth 1 -iname '*.png' -o -iname '*.jpg' -type f`
do
    new=image-$count.${i##*.}

    echo "rename from $i to $new"
    mv "$i" "$new"
    let count++

done

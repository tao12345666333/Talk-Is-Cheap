#!/bin/bash

read -p "Enter random length: " length;

echo "length is ${#length}"

mktemp -u test.$length | cut -d '.' -f 2

#!/bin/bash

echo "Enter random length: "
read length
mktemp -u test.$length | cut -d '.' -f 2

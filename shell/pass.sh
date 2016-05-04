#!/bin/bash
echo -e "passwd: "
stty -echo
read passwd
stty echo
echo
echo passwd is ${passwd}

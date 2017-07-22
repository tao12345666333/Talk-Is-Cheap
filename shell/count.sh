#!/bin/bash
# author: TaoBeier
ss -an|awk '{++s[$1]}END{for (i in s)print i,s[i]}'

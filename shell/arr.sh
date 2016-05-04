#!/bin/bash
declare -A ass_array

ass_array['a']=bash
ass_array['b']=Python

echo ${ass_array[@]}
echo ${!ass_array[@]}

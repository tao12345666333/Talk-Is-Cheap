#!/bin/bash
repeat()
{
    while :;
    do
        $@ && return;
        sleep 30;
    done
}

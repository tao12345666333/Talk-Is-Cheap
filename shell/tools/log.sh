#!/bin/bash

function step::log {
    local OPTS=""
    if [ "$1" = "-n" ]; then
        shift
        OPTS+="-n"
    fi
    GREEN="$1"
    shift
    if [ -t 2 ]; then
        echo -e ${OPTS} "\x1B[92m* ${GREEN}\x1B[39m $*" 1>&2
    else
        echo ${OPTS} "* ${GREEN} $*" 1>&2
    fi
}

case "${1:-}" in
    test)
        step::log "-n" "step1" "test"
        step::log "-n" "test"
        step::log "test" "test"
        step::log "test" "test"
        ;;
    *)
        step::log "not test"
        ;;
esac

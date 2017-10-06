#!/bin/bash
# author: TaoBeier
# via: https://unix.stackexchange.com/questions/261247/how-can-i-get-the-amount-of-available-memory-portably-across-distributions
# Currently, the amount of memory that is available for a new workload, without pushing the system into swap, can be estimated from MemFree, Active(file), Inactive(file), and SReclaimable, as well as the "low" watermarks from /proc/zoneinfo.
#
awk -v low=$(grep low /proc/zoneinfo | awk '{k+=$2} END {print k}') '{a[$1]=$2} END {m=a["MemFree:"]+a["Active(file):"]+a["Inactive(file):"]+a["SReclaimable:"]; print m-12*low}' /proc/meminfo


# LOW_WATERMARK=$(awk '$1 == "low" {LOW_WATERMARK += $2} END {print LOW_WATERMARK * 4096}' /proc/zoneinfo)
# 
# MEMINFO=$(</proc/meminfo)
# 
# MEMINFO_MEMFREE=$(echo "${MEMINFO}" | awk '$1 == "MemFree:" {print $2 * 1024}')
# MEMINFO_FILE=$(echo "${MEMINFO}" | awk '{MEMINFO[$1]=$2} END {print (MEMINFO["Active(file):"] + MEMINFO["Inactive(file):"]) * 1024}')
# MEMINFO_SRECLAIMABLE=$(echo "${MEMINFO}" | awk '$1 == "SReclaimable:" {print $2 * 1024}')
# 
# MEMINFO_MEMAVAILABLE=$((
#   MEMINFO_MEMFREE - LOW_WATERMARK
#   + MEMINFO_FILE - ((MEMINFO_FILE/2) < LOW_WATERMARK ? (MEMINFO_FILE/2) : LOW_WATERMARK)
#   + MEMINFO_SRECLAIMABLE - ((MEMINFO_SRECLAIMABLE/2) < LOW_WATERMARK ? (MEMINFO_SRECLAIMABLE/2) : LOW_WATERMARK)
# ))
# 
# if [[ "${MEMINFO_MEMAVAILABLE}" -le 0 ]]
# then
#      MEMINFO_MEMAVAILABLE=0
# fi

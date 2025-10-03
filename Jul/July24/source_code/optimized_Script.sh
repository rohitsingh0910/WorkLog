#!/bin/bash
set -euo pipefail

log_file="optimized.log"
trap 'echo "Script failed! Check logs." >> $log_file' ERR

log() {
    echo "$(date +%F_%T) - $1" >> $log_file
}

calculate_sum() {
    local sum=$(( $1 + $2 ))
    log "Calculated sum of $1 and $2 = $sum"
    echo $sum
}

log "Script started"
result=$(calculate_sum 10 20)
log "Result: $result"
log "Script finished"

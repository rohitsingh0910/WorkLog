#!/bin/bash

log_file="my_script.log"

echo "Script started at $(date)" >> $log_file
echo "Processing data..." >> $log_file
echo "Script finished at $(date)" >> $log_file

# Print the log
cat $log_file

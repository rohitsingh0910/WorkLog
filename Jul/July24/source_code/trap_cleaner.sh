#!/bin/bash

temp_file="/tmp/my_temp_file"
touch $temp_file

trap 'echo "Cleaning up..."; rm -f $temp_file' EXIT

echo "Created temp file: $temp_file"
sleep 5
echo "Exiting script..."

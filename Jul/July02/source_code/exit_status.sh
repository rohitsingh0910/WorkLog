#!/bin/bash
# Check exit status of a command
ls non_existing_file.txt

if [ $? -ne 0 ]; then
    echo "Command failed!"
else
    echo "Command succeeded!"
fi

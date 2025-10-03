#!/bin/bash
# Create sample file
echo -e "error: failed\nsuccess: done\nerror: crash" > log.txt

# Find 'error' lines
grep "error" log.txt

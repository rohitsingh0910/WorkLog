#!/bin/bash
# Replace 'error' with 'fixed'
echo -e "error: bug\nerror: crash" > bug.txt
sed 's/error/fixed/g' bug.txt

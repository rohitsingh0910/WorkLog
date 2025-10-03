#!/bin/bash
# Sample file
echo -e "Name Age\nRohit 25\nAmit 30" > data.txt

# Print only names
awk '{print $1}' data.txt

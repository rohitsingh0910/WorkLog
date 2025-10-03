#!/bin/bash

str="Hello Bash Scripting"
echo "String length: ${#str}"
echo "Substring (0-5): ${str:0:5}"
echo "Replace Hello with Hi: ${str/Hello/Hi}"

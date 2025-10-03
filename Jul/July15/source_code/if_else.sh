#!/bin/bash

read -p "Enter a number: " num

if [ $num -gt 10 ]; then
  echo "Greater than 10"
elif [ $num -eq 10 ]; then
  echo "Exactly 10"
else
  echo "Less than 10"
fi

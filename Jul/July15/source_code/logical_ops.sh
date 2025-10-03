#!/bin/bash

read -p "Enter age: " age

if [ $age -gt 18 ] && [ $age -lt 60 ]; then
  echo "You are eligible for work."
else
  echo "Not eligible."
fi

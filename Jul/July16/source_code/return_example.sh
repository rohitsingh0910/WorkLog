#!/bin/bash

check_even() {
  if (( $1 % 2 == 0 )); then
    return 0
  else
    return 1
  fi
}

read -p "Enter number: " num
check_even $num
if [ $? -eq 0 ]; then
  echo "$num is Even"
else
  echo "$num is Odd"
fi

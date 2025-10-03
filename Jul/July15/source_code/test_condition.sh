#!/bin/bash

a=5
b=8

if [ $a -lt $b ]; then
  echo "$a is less than $b"
fi

if [ -z "$USER" ]; then
  echo "Username is empty"
else
  echo "Username is $USER"
fi

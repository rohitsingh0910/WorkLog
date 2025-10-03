#!/bin/bash

echo "For loop:"
for i in 1 2 3; do
  echo "Number: $i"
done

echo "While loop:"
count=1
while [ $count -le 3 ]; do
  echo "Count is $count"
  ((count++))
done

echo "Until loop:"
count=1
until [ $count -gt 3 ]; do
  echo "Until count: $count"
  ((count++))
done

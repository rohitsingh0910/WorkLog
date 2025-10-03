#!/bin/bash

arr=("apple" "banana" "cherry")

echo "Looping through array:"
for item in "${arr[@]}"; do
  echo "Fruit: $item"
done

echo "Total fruits: ${#arr[@]}"

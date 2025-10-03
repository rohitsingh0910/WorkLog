#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 arg1 arg2"
  exit 1
fi

echo "Arguments received: $@"

#!/bin/bash

set -x
echo "Debugging enabled"
a=5
b=3
echo "Sum: $((a + b))"
set +x
echo "Debugging disabled"

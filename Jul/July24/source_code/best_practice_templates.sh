#!/bin/bash
# Enable strict mode
set -euo pipefail

# Trap cleanup
trap 'echo "Exiting script...";' EXIT

# Use functions
hello() {
    local name=$1
    echo "Hello, $name!"
}

hello "Rohit"

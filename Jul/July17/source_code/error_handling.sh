#!/bin/bash

set -e  # Exit on error

trap 'echo "An error occurred! Exiting..."' ERR

cp non_existing_file.txt /tmp/ || echo "Copy failed!"  # Example error
echo "This will not run if the above fails due to set -e"

#!/bin/bash
# Demonstrate local vs global variable

my_var="GlobalVar"

print_vars() {
    local my_var="LocalVar"
    echo "Inside function: $my_var"
}

print_vars
echo "Outside function: $my_var"

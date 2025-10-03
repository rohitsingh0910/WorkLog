#!/bin/bash

files=("file1.txt" "file2.txt" "file3.txt" "file4.txt" "file5.txt")

for file in "${files[@]}"; do
    if [[ -e $file ]]; then
        size=$(stat -c %s "$file")
        echo "File '$file' exists. Size: $size bytes."
    else
        echo "File '$file' does not exist."
    fi
done

create_file() {
    touch "$1"
    echo "File '$1' has been created."
}

echo "Do you want to create a missing file? (yes/no)"
read answer

if [[ "$answer" == "yes" ]]; then
    echo "Enter the name of the file to create:"
    read filename
    create_file "$filename"
else
    echo "No file will be created."
fi

echo "File checking complete."

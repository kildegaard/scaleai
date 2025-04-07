#!/bin/bash

# Check if the CSV file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 filename.csv"
    exit 1
fi

filename=$1

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File not found!"
    exit 1
fi

# Read and process the CSV file
awk -F, '
BEGIN {
    print "Name\t\tAmount Spent"
    print "-------------------------"
}
NR > 1 { # Skip the header line
    if ($3 > 18) { # Check if age is greater than 18
        printf "%-15s\t%s\n", $1, $4
    }
}
' "$filename"

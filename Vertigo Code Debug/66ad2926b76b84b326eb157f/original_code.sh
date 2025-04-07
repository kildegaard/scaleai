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
echo -e "Name\t\tAmount Spent\tSpent per Year"
echo "---------------------------------------------"

# Skip the header line and process the rest
tail -n +2 "$filename" | while IFS=, read -r name age email years_worked amount_spent; do
    if [ "$age" -gt 18 ]; then
        spent_per_year=$(echo "scale=2; $amount_spent / $years_worked" | bc)
        printf "%-15s\t%-15s\t%.2f\n" "$name" "$amount_spent" "$spent_per_year"
    fi
done

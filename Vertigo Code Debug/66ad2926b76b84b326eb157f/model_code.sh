#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 filename.csv"
    exit 1
fi

filename=$1

if [ ! -f "$filename" ]; then
    echo "File not found!"
    exit 1
fi

echo -e "Name\t\tAmount Spent\tSpent per Year"
echo "---------------------------------------------"

tail -n +2 "$filename" | while IFS=, read -r name age email years_worked amount_spent; do
    if (( age > 18 )); then
        spent_per_year=$(echo "scale=2; $amount_spent / $years_worked" | bc)
        printf "%-15s\t%-15s\t%.2f\n" "$name" "$amount_spent" "$spent_per_year"
    fi
done
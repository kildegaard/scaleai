#!/bin/bash

if [ ! -f numbers.txt ]; then
    echo "Error: numbers.txt file not found."
    exit 1
fi

numbers=($(tr -d '\r' < numbers.txt))

echo "Values from numbers.txt:"
for num in "${numbers[@]}"; do
    echo $num
done

echo
echo "Dividing odd numbers by the subsequent even numbers:"

for (( i=0; i<${#numbers[@]}; i+=2 )); do
    odd=${numbers[i]}
    even=${numbers[i+1]}
    
    # check if even number is missing
    if [ -z "$even" ]; then
        echo "Error: missing even number for $odd"
        continue
    fi
    
    # check if even number is zero
    if [ $even -eq 0 ]; then
        echo "$odd / $even = undefined (division by zero)"
    else
        result=$(echo "scale=2; $odd / $even" | bc)
        echo "$odd / $even = $result"
    fi
done

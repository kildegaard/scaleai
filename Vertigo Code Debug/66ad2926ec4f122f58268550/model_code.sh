#!/bin/bash

numbers=($(tr -d '\r' < numbers.txt))

echo "Values from numbers.txt:"
for num in "${numbers[@]}"; do
    echo $num
done

echo
echo "Dividing odd numbers by the subsequent even numbers:"

for (( i=0; i<${#numbers[@]}-1; i+=2 )); do
    odd=${numbers[i]}
    even=${numbers[i+1]}
    result=$(echo "scale=2; $odd / $even" | bc)
    echo "$odd / $even = $result"
done
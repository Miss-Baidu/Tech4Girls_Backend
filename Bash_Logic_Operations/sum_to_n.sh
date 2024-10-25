#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 n"
    exit 1
fi
n=$1
if ! [[ "$n" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a positive integer."
    exit 1
fi
sum=0
for (( i=1; i<=n; i++ )); do
    sum=$((sum + i))
done
echo "The sum of numbers from 1 to $n is: $sum"
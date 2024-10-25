#!/bin/bash
echo "enter the number:"
read num
if ! [[ "$num" =~ ^-?[0-9]+$ ]]; then
    echo "Error: Please enter a valid integer."
    exit 1
fi
if [ $((num%2)) -eq 0 ]
then 
    echo "even number"
else
    echo "odd number"
    fi
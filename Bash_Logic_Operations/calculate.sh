#!/bin/bash
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 num1 num2 num3"
    exit 1
fi
num1=$1
num2=$2
num3=$3
sum=$((num1 + num2))
product=$((sum * num3))
echo "The sum of $num1 and $num2 is: $sum"
echo "Multiplying the sum by $num3 gives: $product"
#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <number1> <number2>"
    exit 1
fi
num1=$1
num2=$2
if [ "$num1" -gt 10 ] && [ "$num2" -gt 10 ]; then
    echo "Both numbers are greater than 10."
    elif [ "$num1" -gt 10 ] || [ "$num2" -gt 10 ]; then
    echo "At least one number is greater than 10."
    else
    echo "Neither number is greater than 10."
fi
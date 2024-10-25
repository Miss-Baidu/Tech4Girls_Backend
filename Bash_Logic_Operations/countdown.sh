#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <number>"
  exit 1
fi
if ! [[ "$1" =~ ^[1-9][0-9]*$ ]]; then
  echo "Please enter a positive integer."
  exit 1
fi
for ((i = $1; i >= 1; i--)); do
  echo $i
done

echo "Countdown complete!"
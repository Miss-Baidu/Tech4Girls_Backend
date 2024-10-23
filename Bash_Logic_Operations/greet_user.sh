#!/bin/bash
if [ "$#" -ne 2 ] ; then
echo "Usage:$0 <First_Name> <Last_Name>"
exit 1
fi
First_Name=$1
Last_Name=$2
echo "Hello, [$First_Name] [$Last_Name]! Welcome to Bash scripting."

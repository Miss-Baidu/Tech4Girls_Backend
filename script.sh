#!/bin/bash
#variable_name=$((n1+n2))
# * =multiplication
# / = division
# % = modulo
# ** =exponentiation or power




#the read command
# read variable_name
# echo "what is your name? :"
# read name
# echo "and your age?"
# read age
# echo "what is your password?"
# read -p password:
# echo "Hello $name, You are $age years old,and your password has been saved"

#echo "Hello world $name, You are $age years old, and your password $password has been saved"
#read -p "Enter your first_name and last_name " first_name last_name
#echo "Your name has been recorded as $first_name $last_name"
 
 #posotional Arguments In Bash Scripting
#  $0 = script's name or first argument
#  $1 = second argument
#  $2 = third argument
#echo "Hello, $1, how are you doing?"

# echo "The first argument or the name of the script is:$0"
# echo "The second argument is:$1"
# echo "The third argument is:$3" 
# echo "The fourth argument is:$4"

# sum=$(($1 + $2))
# echo "The sum  of $1 and $2 is: $sum"
# diff=$(($1 -$2))
# echo "The diff of $1 and $2 is: $diff"
# multiplication=$(($1 * $2))
# echo "The multiplcation of $1 and $2:$multiplication"

# touch file2
# mkdir folder2
# cp "$1" "$2"
# echo "$1 has been moved into $2"

#LOGICAN OR = ||
#LOGICAL AND = &&
#LOGICAL NOT = !

#IF STATEMENTS IN BASH
# if [ condition ]
#  then
#       statement
# fi
# echo "how old are you"
# read age

# age=30
# if [ "$1" -gt 10 ] && [ "$2" -gt 10 ]
# then
#     echo "Both numbers are greater than 10"
# else 
#     echo "One or both numbers are not greater than 10"
# fi

# string="Hi,Ladies!"

# if [[ ! $string == "Goodbye!" ]]
# then 
#     echo "String is not equal to goodbye"
# else 
    #echo "string is not equal to goodbye"
# fi

# echo "What's your name?"
# read username
# if [[ ! $username == "Admin" ]]
# then
# echo "Acess denied"
# else
# echo "Acess granted"
# fi

# WHILE LOOP IN BASH
# while [ condition ]
# do 
#    [ command ]
#     [ command ]
#      [ command ]
#done

# number=1

# while [ $number -le 10 ]
# do
#    echo "$number"
#    number=$((number+1))
# done

# while true; do
#    echo "Enter a number or type "q" to quit"
#    read number

#    if [[ "$number" == 'q' ]];then
#      break
#   fi

#    echo "You entered $number"
# done

# echo "Exiting the loop"
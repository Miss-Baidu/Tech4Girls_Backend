#!/usr/bin/python3
age = int(input("How old are you? : "))

if age < 18:
    print("You are a minor.")
elif 18 <= age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")

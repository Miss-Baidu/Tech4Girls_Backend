# Error and Exception Handling in Python

# Example of Synthax error
# print ("Hello Girls")

# Exception block refers to the part of code used for handling exceptions or errors that may occur during the execution of a program.
# try except : used to handle the exceptions
# An exception in Python (and in programming in general) is an event that disrupts the normal flow of a program's execution. It usually occurs when the program encounters an error or an unexpected situation that it cannot handle under normal conditions.

#TPYES OF EXCEPTIONS
# Zero Division Execption :Occours when you try to divide a number by zero
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Idiot , you can not divide by zero")
# print("Hello World")

# print("Give me two numbers and I will divide them")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) /int (second_number)
#     except ZeroDivisionError:
#         print("Idiot , you can not divide by zero")
#     except ValueError:
#         print("Numbers only Dumbo!")
#     except Exception as e:
#         print (e)
#     else:
#         print(answer)
#     finally:
#         print("Goodbyee")

# TYPE ERROR : Happens when you try to concatenate a str and int
# Result = "1" + 2
# print(Result)

# FINALLY BLOCK : 
#PASS : IGNORES ALL EXCEPTION

# VALUE ERROR :Occurs when appopriate type but inappopriate value

# values = [10, 9, 8, 0, 5]
# for value in values:
#     try:
#         print(10 / value)
#     except:
#         pass

# INDEX ERROR : 
# try:
#     my_list = [1, 2, 3]
# except IndexError:
#     print("Number not in range")
# else:
#     print("No error occured")

def calculate_average(numbers):
    #Calculates the average of a list of numbers
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_numbers():
    #Gets a list of numbers from user
    numbers = []
    while True:
        user_input = input("Enter numbers or type 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        number_strings = user_input.split()
        for number_string in number_strings:
            number = int(number_string)
            numbers.append(number)
        return numbers

if __name__ == "_main_":
    try:
       numbers = get_numbers()
       if numbers:
          average = calculate_average(numbers)
          print(f"The average is: {average}")
       else:
          print("No numbers entered.")
    except ZeroDivisionError:
          print("Cannot calculate average of 0")
    except Exception:
          print("An unexcepted error occured")
     
        
    
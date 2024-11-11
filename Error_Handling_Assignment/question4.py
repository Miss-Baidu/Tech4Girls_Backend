# Question 5: List Index Access
items = ["apple", "banana", "cherry"]
try:
    index = int(input("Enter the index of the item you want to access: "))
    print("You selected:", items[index])
except IndexError:
    print("This index is out of range. Please enter a valid index")
except ValueError:
    print("Error: Please enter a valid integer.")

# Question 1: Division Calculator
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Error: Denominator can not be equal to 0")
    else:
        result = numerator / denominator
        print("The result is:", result)

except ValueError:
        print("Error: Input valid integers for both the numerator and denominator")

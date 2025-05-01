'''Write a program that reads a number and reports whether it is positive,
negative or zero.'''
# Initialize a variable to store the number
num = float(input("Enter a number: "))

# Check if the number is positive, negative or zero and display the result
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
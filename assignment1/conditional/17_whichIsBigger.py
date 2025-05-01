'''Write a program that reads two numbers and tells you which one is
bigger.'''
# Initialize two variables to store the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Compare the two numbers and display the result
if num1 > num2:
    print("The first number is bigger.")
elif num1 < num2:
    print("The second number is bigger.")
else:  
    print("Both numbers are equal.")
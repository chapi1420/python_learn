'''Write a program that asks the user for three numbers and displays the
largest one.'''

# Initialize three variables to store the three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the three numbers and display the largest one
if num1 >= num2 and num1 >= num3:
    print("The first number is the largest.")
elif num2 >= num1 and num2 >= num3:
    print("The second number is the largest.")
elif num3 >= num1 and num3 >= num2:
    print("The third number is the largest.")
else:
    print("All numbers are equal.")

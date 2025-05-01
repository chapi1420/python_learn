"""Write a program that calculates the geometric mean of three
numbers entered by the user"""
#
# Initialize three variables to store the three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Calculate the geometric mean
geometric_mean = (num1 * num2 * num3) ** (1/3)
# Display the result
print("Geometric mean: ", geometric_mean)
"""Create a program that calculates and displays the arithmetic
mean of three grades entered by the user."""

num1, num2, num3 = input("Enter three grades separated by spaces: ").split()
# Convert the input to float
num1 = float(num1)  
num2 = float(num2)  
num3 = float(num3)  
# Calculate the arithmetic mean
arithmetic_mean = (num1 + num2 + num3) / 3
# Display the result
print("Arithmetic mean: ", arithmetic_mean)
'''Create a program that reads three numbers and checks if their sum is
positive, negative or equal to zero'''

# Initialize three variables to store the three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the sum of the three numbers
sum_of_numbers = num1 + num2 + num3

#check if the sum is positive, negative or zero and display the result
if sum_of_numbers > 0:
    print("The sum of the three numbers is positive.")
elif sum_of_numbers < 0:
    print("The sum of the three numbers is negative.")
else:
    print("The sum of the three numbers is zero.")
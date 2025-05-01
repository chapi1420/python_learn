'''Make a program that reads three numbers, and informs if their sum is
divisible by 5 or not.'''

# take input of the three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# calculate the sum of the three numbers
sum_of_numbers = num1 + num2 + num3

#check if the sum is divisible by 5
if sum_of_numbers % 5 == 0:
    print("The sum of the three numbers is divisible by 5.")
else:
    print("The sum of the three numbers is not divisible by 5.")
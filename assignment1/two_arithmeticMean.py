'''Write a program that calculates the arithmetic mean of two
numbers.
'''
#initialize two variables to store the two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
#convert the input to float
num1 = float(num1)      

num2 = float(num2)
#calculate the arithmetic mean
arithmetic_mean = (num1 + num2) / 2
#display the result
print("Arithmetic mean: ", arithmetic_mean)
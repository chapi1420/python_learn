'''1. Write a program that prompts the user for two numbers and
displays the addition, subtraction, multiplication, and division
between them.'''

#initialixe two variables to store the two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
#convert the input to float
num1 = float(num1)
num2 = float(num2)
#calculate addition, subtraction, multiplication and division
addition = num1 + num2  
subtraction = num1 - num2
multiplication = num1 * num2    
division = num1 / num2
#display the results
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
 

'''Write a program that prompts the user for two numbers A
and B and displays all numbers between A and B.'''

# Prompt the user for two numbers A and B
a = int(input("Enter the first number (A): "))
b = int(input("Enter the second number (B): "))

if a<b-1: 
    print(range(a, b))

elif b<a-1: print(range(b, a))

else: print('there is no number between A and B')
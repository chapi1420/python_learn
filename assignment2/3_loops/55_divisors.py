'''Write a program that prompts the user for a number and
displays its divisors.'''

#take input from the user
number = int(input("Enter a number: "))

#initialize a list to store the divisors
divisors = []
#loop through the range from 1 to the number
for i in range(1, number + 1):
    #check if the number is divisible by i
    if number % i == 0:
        #if it is, append it to the list of divisors
        divisors.append(i)
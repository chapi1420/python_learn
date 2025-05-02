'''Write a program that asks the user for a number N and
displays the sum of all numbers from 1 to N.'''

#take input from user
num = int(input('Enter a number: '))

#initialize sum to 0
sum = 0

#loop from 1 to N
for i in range(1, num + 1):
    #add each number to sum
    sum += i

#display the sum
print(f'The sum of numbers from 1 to {num} is {sum}')
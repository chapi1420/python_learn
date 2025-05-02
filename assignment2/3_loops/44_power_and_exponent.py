'''Write a program that calculates and displays the value of
the power of a number entered by the user raised to an
exponent also entered by the user, using repetition loops.'''

num = int(input('Enter a number: '))
exponent = int(input('Enter the exponent: '))
result = 1

for i in range(1,exponent+1):
    result *= num
print(f'The result of {num} raised to the power of {exponent} is {result}.')
'''Write a program that prompts the user for a number and
displays the Fibonacci sequence up to the given number using a
repeating loop.'''

num = int(input('Enter a number: '))
a, b = 0, 1

print('Fibonacci sequence:')
while a <= num:
    print(a, end=' ')
    a, b = b, a + b  
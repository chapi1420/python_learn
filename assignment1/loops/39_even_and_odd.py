'''Write a program that displays even numbers 1 to 50 and
odd numbers 51 to 100 using a repeating loop.'''

for i in range(1, 101):
    if i <= 50 and i % 2 == 0:
        print(i, end=' ')
    elif i > 50 and i % 2 != 0:
        print(i, end=' ')
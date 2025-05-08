'''Write a program that reads numbers from the user until a
negative number is entered, and prints the sum of the positive
numbers.'''

sum = 0

while True:
    num = float(input('insert a number, press negative to stop'))
    if num < 0:
        break
    sum += num
print('sum:', sum)


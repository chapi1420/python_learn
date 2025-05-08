'''Write a program that prompts the user for a list of
numbers, until the user types the number zero, and displays the
largest and smallest numbers in the list.'''

# Prompt the user for a list of numbers until zero is entered
numbers = []

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    numbers.append(number)

minim = numbers[0]
maxim = numbers[0]

for i in numbers:
    if minim > i:
        minim = i
    if maxim < i:
        maxim = i
print('minimum:', minim)
print('maximum:', maxim)
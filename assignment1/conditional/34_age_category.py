'''Create a program that asks for a person's age and displays whether they
are a child (0-12 years old), teenager (13-17 years old), adult (18-59 years old),
or elderly (60 years old or older).'''

# take input from the user
age = int(input('Enter your age: '))


# check the age category
if age >= 0 and age <= 12:
    print('Child')
elif age >= 13 and age <= 17:
    print('Teenager')
elif age >= 18 and age <= 59:
    print('Adult')
elif age >= 60:
    print('Elderly')
else:
    print('Invalid age entered. Please enter a non-negative integer.')
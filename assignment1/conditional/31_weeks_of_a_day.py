'''Write a program that asks for the name of a day of the week and displays
whether it is a weekday (Monday to Friday) or a weekend day (Saturday and
Sunday).'''

name = input('enter the week day you want to know about:').lower()
if name == 'saturday' or name == 'sunday':
    print(name, 'is a weekend day')
else:
    print(name, 'is a weekday')
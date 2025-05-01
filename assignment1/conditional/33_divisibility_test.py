'''33. Write a program that asks for an integer and checks if it is divisible by 3
and 5 at the same time.'''

# Prompt the user for an integer
number = int(input("Enter an integer: "))

#check if the number is divisible by 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else: 
    print('number not divisible by 3 and 5')
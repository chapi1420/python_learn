'''Make a program that reads the year of birth of a person and informs if he
is able to vote (age greater than or equal to 16 years old).'''
#import necessary library
from datetime import date

# take the year of birth
YOB = int(input("Enter the year of birth: "))

#compute the age of the person
age = date.now().year - YOB

#check if the person is able to vote
if age>16:
    print('eligible to vote')
else:
    print('not eligible to vote')
'''Make a program that reads a person's age and informs if he is not able to
vote (age less than 16 years old), if he is able to vote but is not obligated (16,
17 years old, or age equal to or greater than 70 years), or if it is obligatory (18
to 69 years old).'''

# Import necessary library
from datetime import date

# Take the date of birth
YOB = int(input('Enter your year of birth (YYYY): '))

# Compute the age of the person
current_year = date.today().year
age = current_year - YOB

# Check if the person is not able to vote
if age < 16:
    print('Not able to vote')
elif age >= 16 and (age <= 17 or age >= 70):
    print('Able to vote but not obligated')
else: 
    print('Obligatory to vote')

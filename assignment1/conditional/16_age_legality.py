'''Make a program that asks for a person's age and displays whether they
are of legal age or not.'''
# Prompt the user for their age
age = int(input("Enter your age: "))

# Check if the age is greater than or equal to 18
if age >= 18:
    # If true, the person is of legal age
    print("You are of legal age.")
else:
    # If false, the person is not of legal age
    print("You are not of legal age.")
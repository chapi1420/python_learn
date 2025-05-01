'''Make a program that reads the age of three people and how many of them
are of legal age (age 18 or older).'''
#take the age of three people
age_list = []
for i in range(3):
    age = int(input("Enter the age of person {}: ".format(i + 1)))
    age_list.append(age)

#check how many of them are of legal age    
legal_age_count = 0
for age in age_list:
    if age >= 18:
        legal_age_count += 1

print('the number of legal age people is: ', legal_age_count)
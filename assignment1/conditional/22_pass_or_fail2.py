'''Make a program that reads the grades of two tests, calculates the simple
arithmetic mean, and informs whether the student passed (average greater
than or equal to 6) or failed (average less than 6).'''

#take input of the scores of the two tests
score1 = float(input("Enter the score of the first test: "))
score2 = float(input("Enter the score of the second test: "))

#calculate the arithmetic mean
arithmetic_mean = (score1 + score2) / 2

#display the result
print("The arithmetic mean is: ", arithmetic_mean)

#check if the arithmetic mean is greater than or equal to 6
if arithmetic_mean >= 6:
    print("The student passed.")
else:
    print("The student failed.")

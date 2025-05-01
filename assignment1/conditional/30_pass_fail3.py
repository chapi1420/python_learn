'''Make a program that reads three grades from a student and reports
whether he passed (final grade greater than or equal to 7), failed (final grade
less than 4) or was in recovery (final grade between 4 and 7).'''

#take the scores of the three tests
s1 = float(input("Enter the score of the first test: "))
s2 = float(input("Enter the score of the second test: "))
s3 = float(input("Enter the score of the third test: "))    

#calculate the final grade
final_grade = (s1 + s2 + s3) / 3
print("The final grade is: ", final_grade)

#check if the final grade is greater than or equal to 7
if final_grade >= 7:
    print("The student passed.")
elif final_grade < 4:
    print("The student failed.")    
else:
    print("The student is in recovery.")    
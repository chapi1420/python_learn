'''Write a program that calculates the BMI of an individual,
using the formula BMI = weight / height2'''
# Initialize two variables to store the weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


# Calculate the BMI
bmi = weight / (height ** 2)
# Display the result
print("Your BMI is: ", bmi)
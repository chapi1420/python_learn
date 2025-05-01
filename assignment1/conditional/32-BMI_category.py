'''Write a program that asks for a person's height and weight and calculates
their body mass index (BMI), displaying the corresponding category
(underweight, normal weight, overweight, obese, severely obese).'''

# Prompt the user for their height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI using the formula BMI = weight / height^2
bmi = weight / (height ** 2)

# Display the BMI value
print("Your BMI is: ", bmi)


# Determine the BMI category based on the calculated value
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:  
    category = "Overweight"
elif 30 <= bmi < 34.9:
    category = "Obese (Class 1)"
elif 35 <= bmi < 39.9:
    category = "Obese (Class 2)"
else:
    category = "Obese (Class 3)"


# Display the BMI category
print("Your BMI category is: ", category)
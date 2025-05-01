'''
Write a program that calculates the area of a circle from the
radius, using the formula A = πr2'''
# Import the math module to use the constant pi
import math
# Prompt the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))
# Calculate the area of the circle using the formula A = πr2
area = math.pi * (radius ** 2)
# Display the result
print("The area of the circle is: ", area)

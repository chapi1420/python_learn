'''
Create a program that calculates and displays the perimeter
of a circle, prompting the user for the radius.'''
#
# Import the math module to use the constant pi
import math
# Prompt the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))
# Calculate the perimeter of the circle using the formula P = 2 * pi * r
perimeter = 2 * math.pi * radius
# Display the result
print("The perimeter of the circle is: ", perimeter)
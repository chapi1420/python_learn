'''Create a program that prompts the user for the radius of a
sphere and calculates and displays its volume.'''

# Import the math module to use the constant pi
import math

# take input from the user
radius = float(input('insert tha length of the radius of the sphere: '))

#calculate the volume
volume = (4/3) * math.pi * (radius ** 3)

# display the result
print('The volume of the sphere is: ', volume)
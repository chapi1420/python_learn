'''Write a program that calculates the kinetic energy of a
moving object, using the formula E = (mv2) / 2, where E is the
kinetic energy, m is the mass of the object, and v is the velocity.'''

# Prompt the user for the mass of the object and its velocity
mass = float(input("Enter the mass of the object (in kg): "))
velocity = float(input("Enter the velocity of the object (in m/s): "))

#calculate the kinetic energy using the formula E = (mv2) / 2
E = (mass * (velocity ** 2)) / 2
 
# Display the result
print("The kinetic energy of the object is: ", E, "Joules")

'''Write a program that calculates the work done by a force
acting on an object, using the formula T = F * d, where T is the
work, F is the applied force, and d is the distance traveled by
the object.'''

# Prompt the user for the applied force and distance traveled
force_app = float(input("Enter the applied force (in Newtons): "))
distance = float(input("Enter the distance traveled (in meters): "))

#compute the work done
T = force_app*distance

#print the result
print("The work done is: ", T, "Joules")
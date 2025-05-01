'''Write a program that calculates the delta of a quadratic
equation (Δ = b2 - 4ac).'''
# Initialize three variables to store the coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
# Calculate the delta of the quadratic equation
delta = b ** 2 - 4 * a * c
# Display the result
print("The delta of the quadratic equation is: ", delta)
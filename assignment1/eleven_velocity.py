'''Write a program that calculates the average velocity of an
object, using the formula v = Δs/Δt, where v is the average
velocity, Δs is the space variation, and Δt is the time variation'''

# Prompt the user for the space variation and time variation
space_variation = float(input("Enter the space variation (Δs): "))
time_variation = float(input("Enter the time variation (Δt): "))

# Calculate the average velocity using the formula v = Δs/Δt
average_velocity = space_variation / time_variation

# Display the result
print("The average velocity is: ", average_velocity)

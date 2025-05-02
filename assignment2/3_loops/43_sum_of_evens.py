'''Write a program that calculates and displays the sum of
even numbers from 1 to 100 using a repeating loop.'''

# Initialize sum to 0
sum_of_evens = 0

# Initialize counter to 1
counter = 1

# Loop from 1 to 100
while counter <= 100:
    # Check if the number is even
    if counter % 2 == 0:
        # Add to sum_of_evens
        sum_of_evens += counter
    # Increment counter
    counter += 1
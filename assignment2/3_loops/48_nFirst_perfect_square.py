'''Create a program that displays the first N first perfect
squares, where N is informed by the user, using a loop.'''

# Function to display the first N perfect squares
def display_perfect_squares(N):
    for i in range(1, N + 1):
        perfect_square = i ** 2
        print(perfect_square)

# Main program
if __name__ == "__main__":
    try:
        N = int(input("Enter the number of perfect squares to display: "))
        if N > 0:
            print(f"The first {N} perfect squares are:")
            display_perfect_squares(N)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

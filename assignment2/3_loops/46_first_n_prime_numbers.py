'''Write a program that prompts the user for a number N and
displays all prime numbers less than N.'''


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to display all prime numbers less than N
def display_primes_less_than(N):
    print(f"Prime numbers less than {N}:")
    for num in range(2, N):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    try:
        N = int(input("Enter a number N to display all prime numbers less than N: "))
        if N > 1:
            display_primes_less_than(N)
        else:
            print("Please enter a number greater than 1.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

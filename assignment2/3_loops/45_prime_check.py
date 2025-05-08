'''Write a program that asks the user for a number N and
says whether it is prime or not.'''

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        N = int(input("Enter a number N to check if it is prime: "))
        if is_prime(N):
            print(f"{N} is a prime number.")
        else:
            print(f"{N} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

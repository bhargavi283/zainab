def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Input from user
n = int(input("Enter the value of n: "))

# Get first n prime numbers
prime_numbers = find_primes(n)

# Print the prime numbers
print(f"First {n} prime numbers are: {prime_numbers}")

# Print the required statement
print("\nBhargavi patil 0863CS221047")
# Function to calculate square root using Newton's method
def newton_sqrt(number):
    # Initial guess
    guess = number / 2.0
    # Tolerance for stopping criteria
    tolerance = 0.00001
    
    # Loop until the absolute difference between guess and the true square root is within tolerance
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2.0
        
    return guess

# Input: Getting a number from the user
number = float(input("Enter a number to find the square root: "))

# Perform the square root calculation using Newton's method
sqrt_result = newton_sqrt(number)

# Output the result
print(f"The square root of {number} is approximately {sqrt_result}")

# Print the required statement
print("\nBhargavi patil 0863CS221047")
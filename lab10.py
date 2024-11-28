# Function to find the maximum number from a list
def find_maximum(numbers):
    return max(numbers)

# Input: Getting a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find the maximum number
max_num = find_maximum(numbers)

# Output the result
print(f"The maximum number in the list is {max_num}")

# Print the required statement
print("\nBhargavi patil 0863CS221047")
# Linear Search in Python

# Function to perform linear search
def linear_search(arr, target):
    # Loop through each element in the list
    for i in range(len(arr)):
        # Check if the current element is equal to the target
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Input: Getting the list of numbers from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Input: Getting the number to search for
target = int(input("Enter the number to search for: "))

# Perform the search
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"The number {target} is found at index {result}.")
else:
    print(f"The number {target} is not found in the list.")

print("\nBhargavi patil 0863CS221047")   
# Binary Search in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle element
        
        # Check if target is at the mid position
        if arr[mid] == target:
            return mid
        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            high = mid - 1
        # If target is larger, ignore the left half
        else:
            low = mid + 1
            
    return -1  # Target is not in the array

# Input: Getting a sorted list of numbers from the user
arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))

# Input: Getting the number to search for
target = int(input("Enter the number to search for: "))

# Perform the binary search
result = binary_search(arr, target)

# Output the result
if result != -1:
    print(f"The number {target} is found at index {result}.")
else:
    print(f"The number {target} is not found in the list.")

# Print the required statement
print("\nBhargavi patil 0863CS221047")
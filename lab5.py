# Insertion Sort in Python

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input: Getting a list of numbers from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Perform the insertion sort
insertion_sort(arr)

# Output the sorted array
print("Sorted array is:", arr)

# Print the required statement
print("\nBhargavi patil 0863CS221047")
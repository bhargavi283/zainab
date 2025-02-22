# Selection Sort in Python

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input: Getting a list of numbers from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Perform the selection sort
selection_sort(arr)

# Output the sorted array
print("Sorted array is:", arr)

# Print the required statement
print("\nBhargavi patil 0863CS221047")
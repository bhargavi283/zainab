# Merge Sort in Python

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left in L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Checking if any element was left in R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Input: Getting a list of numbers from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Perform the merge sort
merge_sort(arr)

# Output the sorted array
print("Sorted array is:", arr)

# Print the required statement
print("\nBhargavi patil 0863CS221047")
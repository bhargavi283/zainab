# Function to multiply two matrices
def multiply_matrices(A, B):
    # Get the number of rows and columns
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Check if multiplication is possible
    if cols_A != rows_B:
        return "Matrix multiplication is not possible due to incompatible dimensions."

    # Create a result matrix initialized with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Input: Getting matrices from the user
print("Enter the elements of the first matrix (A):")
rows_A = int(input("Enter number of rows for matrix A: "))
cols_A = int(input("Enter number of columns for matrix A: "))
A = [list(map(int, input(f"Enter row {i+1} of matrix A: ").split())) for i in range(rows_A)]

print("\nEnter the elements of the second matrix (B):")
rows_B = int(input("Enter number of rows for matrix B: "))
cols_B = int(input("Enter number of columns for matrix B: "))
B = [list(map(int, input(f"Enter row {i+1} of matrix B: ").split())) for i in range(rows_B)]

# Perform matrix multiplication
result = multiply_matrices(A, B)

# Output the result
if isinstance(result, str):
    print(result)  # In case multiplication is not possible
else:
    print("\nThe result of matrix multiplication is:")
    for row in result:
        print(row)

# Print the required statement
print("\nBhargavi patil 0863CS221047")
import numpy as np
def swap_row(M, a, b):
    if type(M) == np.ndarray:
        temp = M[a].copy()
        M[a] = M[b]
        M[b] = temp
def swap_col(M, a, b):
    if type(M) == np.ndarray:
        temp = M[:,a].copy()
        M[:,a] = M[:,b]
        M[:,b] = temp
# Example usage
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:")
print(M)
swap_row(M, 0, 1)
print("After swapping rows 0 and 1:")
print(M)
swap_col(M, 0, 2)
print("After swapping columns 0 and 2:")
print(M)
# Output:
# Original Matrix:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]  
# After swapping rows 0 and 1:
# [[4 5 6]
#  [1 2 3]
#  [7 8 9]]
# After swapping columns 0 and 2:
# [[6 5 4]
#  [3 2 1]  
#  [9 8 7]]
# Note: The swap functions modify the matrix in place. 
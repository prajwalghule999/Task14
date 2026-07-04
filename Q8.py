import numpy as np 

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

print("Element-wise Multiplication:", A * B)
print("Matrix Multiplication:", A @ B)

# Difference:
    # '*' multiplies corresponding elements of the two matrices.
    # '@' or np.dot() performs matrix multiplication using
    # rows of the first matrix and columns of the second matrix.

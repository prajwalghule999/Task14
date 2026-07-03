import numpy as np 

arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])


print("Original Array:")
print(arr)

# Extract first row
print("\nFirst Row:")
print(arr[0])

# Extract last column
print("\nLast Column:")
print(arr[:, 3])

# Extract center 2x2 submatrix
print("\nCenter 2x2 Submatrix:")
print(arr[1:3, 1:3])

# Extract all even numbers using boolean indexing
print("\nEven Numbers:")
print(arr[arr % 2 == 0])
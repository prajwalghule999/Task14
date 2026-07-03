import numpy as np 

 # Create a 5x5 matrix with random integers between 1 and 100
arr = np.random.randint(1, 101, (5, 5))

print("Original Matrix:")
print(arr)

# Print diagonal elements
print("\nDiagonal Elements:")
print(np.diag(arr))

# Print elements greater than 50
print("\nElements Greater Than 50:")
print(arr[arr > 50])

# Replace elements less than 30 with 0
arr[arr < 30] = 0

# Print modified array
print("\nModified Matrix:")
print(arr)
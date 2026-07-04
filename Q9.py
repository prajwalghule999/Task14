import numpy as np

arr = np.random.randn(6,6)
print(arr)
print("Shape :",arr.shape)
print("Size :", arr.size)
print("DataType :",arr.dtype)
print("Minimum Value :",np.min(arr),"Index :",np.argmin(arr))
print("Maximum Value :",np.max(arr),"Index :",np.argmax(arr))

submatrix = arr[:3, :3]
print("\nTop-Left 3x3 Submatrix:\n", submatrix)

# Replace all negative numbers with their absolute value
arr = np.abs(arr)

print("\nModified Matrix (Negative values replaced):\n", arr)

# Print mean of modified matrix
print("\nMean of Modified Matrix:", np.mean(arr))
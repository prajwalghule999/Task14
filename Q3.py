import numpy as np 

arr = np.random.randint(20,80,(4,5))
print(arr)

print("Maximum value of Matrix :",np.max(arr))
print("Minimum value of Matrix :",np.min(arr))
print("Sum of Matrix :",np.sum(arr))
print("Mean :",np.mean(arr))
print("Standard Deviation :",np.std(arr))

# Sum of each row
print("\nSum of Each Row:")
print(np.sum(arr, axis=1))

# Sum of each column
print("\nSum of Each Column:")
print(np.sum(arr, axis=0))
import numpy as np

arr = np.arange(1,25)
print(arr)
print(arr.shape)

print("Reshaped array into (4, 6)")
arr2 = arr.reshape(4,6)
print(arr2)
print("Shape :",arr2.shape)

print("Reshaped array into (3, 8)")
arr3 = arr.reshape(3,8)
print(arr3)
print("Shape :",arr3.shape)

print("Reshaped array into (2, 3, 4) (3D array)")
arr4 = arr.reshape(2, 3, 4)
print(arr4)
print("Shape :",arr4.shape)
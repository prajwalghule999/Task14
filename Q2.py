import numpy as np 

arr = np.random.randint(1,50,20)
print(arr)

print("Maximun value :",np.max(arr))
print("Index :",np.argmax(arr))

print("Minimum value :",np.min(arr))
print("Index :",np.argmin(arr))

print("Sum of all elements :",np.sum(arr))
print("Mean :",np.mean(arr))
print("Standard Deviation :",np.std(arr))
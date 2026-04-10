import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("Array a:", a)
print("Array b:", b)
print("Sum", a+b)
print("Multiply:", a*b)
print("Mean of a:", np.mean(a))
print("Mean of b:", np.max(b))

matrix = np.array([[1,2,3], [4,5,6]])
print("Matrix shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)

print("First element of a:", a[0])
print("Last element of a:", a[-1])
print("First row of matrix:", matrix[0])
print("Element at row 1, col2:", matrix[1][2])

reshaped = a.reshape(5,1)
print("Reshaped a:", reshaped)
print("Reshaped shape:", reshaped.shape)

b = np.array([10,20,30,40,50])
print("Sum without loop:", a+b)
print("Multiply without Loop:", a*b)

print("Mean:", np.mean(a))
print("Standard Deviation:", np.std(a))
print("Min", np.min(a))
print("Max", np.max(a))
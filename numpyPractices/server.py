import numpy as np


arr = np.zeros(10, dtype=int)
print(arr)

arr = np.ones(10, dtype=int)
print(arr)

arr = np.full(10, 5)
print(arr)

arr = np.arange(10,51)
print(arr)

arr = np.arange(10,51,2)
print(arr)

arr = np.array([[0,1,2], [3,4,5], [6,7,8]])
print(arr)

identityArray = np.identity(3, dtype=int)
print(identityArray)

randNumBet0and1 = np.random.uniform(0,1)
print(randNumBet0and1)

# rand array of 25
arr = np.random.rand(25)
print(arr)

# between 0 and 1 - 100 even partitions
arr = np.linspace(0,1,100)
arr10x10 = arr.reshape(10, 10)
print(arr10x10)

# linear space between 0 and 1
arr = np.linspace(0,1,20)
print(arr)

mat = np.arange(1,26).reshape(5,5)
print(mat)

subsection = mat[2:5,1:5]
print(subsection)

subsectionIndVal = mat[3,4]
print(subsectionIndVal)

columnOfMatrix = mat[0:3,1:2]
print(columnOfMatrix)

subsection = mat[3:5, 0:5]
print(subsection)

matSum = mat.sum()
print(matSum)

matStdDev = mat.std()
print(matStdDev)

matSumColumns = np.sum(mat, axis=0)
print(matSumColumns)




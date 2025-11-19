import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import matplotlib.pyplot as plt

mystery_array = np.array(
    [
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7]
        ],

        [
            [7, 86, 6, 98],
            [5, 1, 0, 4]
        ],
        [
            [5, 36, 32, 48],
            [97, 0, 27, 18]
        ]
    ]
)

# narray has three dimensions
print(f"Mystery array Dimensions: {mystery_array.ndim}")

# narray has 3 X 2 X 4 elements
print(f"Mystery array shape: {mystery_array.shape}")

print(f"{mystery_array[2][1]}")

print(f"{mystery_array[:, :, 0]}")


# utilization of arange()
a = np.arange(10, 30)
print(a)
print(a[17:])
subsetOfA = (a[3:6])
print(subsetOfA)
# evenNumbersOnly = a[a % 2 == 0]
# print(evenNumbersOnly)
print(a[::2])

# reverse array
reverseA = np.flip(a)
print(reverseA)

#indices having non zero values
checkForNonZero = np.array([6,0,9,0,0,5,0])
print(np.where(checkForNonZero != 0))

# generate 3x3x3 array of random values
random3x3 = np.random.rand(3,3,3)
print(random3x3)

# vector of size 9 with evenly spaced values bretween 0 and 100
print(np.linspace(0, 100, 9))

# vector of size 9 with evenly spaced values bretween -3 and 3
neg3and3 = np.linspace(-3, 3, 9)
print(neg3and3)
# plt.plot(neg3and3) 
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.title("-3 to 3 spaced values")
# plt.show()

# noise = np.random.rand(128, 128, 3)
# plt.imshow(noise)
# plt.show()

# linear algebra

a1 = np.array([
    [1,3],
    [0,1],
    [6,2],
    [9,7],
]);

a2 = np.array([
    [4,1,3],
    [5,8,5]
]);

result = np.matmul(a1, a2)

print(result)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

x = np.arange(0,100)
y = x * 2
z = x**2
print(x)
print(y)
print(z)

# fig = plt.figure()
# ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
# ax1.set_xlabel('X Label')
# ax1.set_ylabel('Y Label')
# ax1.set_title('X - Y Chart')
# ax1.plot(x,y)

# ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
# ax2.plot(x,y)
# plt.show()

# fig = plt.figure()
# ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
# ax1.plot(x, z, color='greed')


# fig, axes = plt.subplots(nrows=1, ncols=2)
# axes[0].plot(x,y, lw=3, linestyle='--', color="b")
# axes[1].plot(x,z, lw=3, color="r")
# plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9,2))
axes[0].plot(x,y, lw=3, color="b")
axes[1].plot(x,z, lw=3, linestyle='--', color="red")
plt.show()
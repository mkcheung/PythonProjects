import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

workingDirectory = Path(__name__).resolve().parent

dataFrame = pd.read_csv(f"{workingDirectory}/df3")
# print(dataFrame.info())

# panda scatter plot
# dataFrame.plot.scatter(x='a',y='b', color='red', figsize=(12,4))

# panda histogram
# dataFrame.hist('a', bins=10)
# dataFrame['a'].plot.hist(bins=10)

# panda box plot
# dataFrame['d'].plot.kde(lw=3, linestyle='--')

# panda area plot
dfUpTo30 = dataFrame.iloc[0:31]
dfUpTo30.plot.area()
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.show()
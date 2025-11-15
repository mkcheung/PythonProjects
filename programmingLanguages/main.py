import matplotlib.pyplot as plt
import os
from pathlib import Path
import pandas as pd

workingDirectory = Path(__file__).resolve().parent 
df = pd.read_csv(f"{workingDirectory}/QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
df.DATE = pd.to_datetime(df.DATE)
pivoted_df = df.pivot(index='DATE', columns="TAG", values="POSTS")
columns = pivoted_df.columns
roll_df = pivoted_df.rolling(window=6).mean()
plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in columns:
    plt.plot(pivoted_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
    
plt.legend(fontsize=16)
plt.show()
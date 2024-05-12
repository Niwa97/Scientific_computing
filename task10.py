import pandas as pd
import numpy as np

#2
x = np.datetime64('2024-05-01')
rng = np.random.default_rng()
rand_list = rng.integers(low=-1, high=1, size=31).tolist()
rand_walk_in_may = [10]
for i in range(30):
  rand_walk_in_may.append(rand_walk_in_may[i] + rand_list[i])
ind = [x + i for i in range(31)]
s1 = pd.Series(rand_walk_in_may, index=ind)
print(s1)

#3
df = pd.read_csv('elements.csv', header=0, nrows=11, sep = ';')
df.index += 1
print(df.columns)
print(df.index)

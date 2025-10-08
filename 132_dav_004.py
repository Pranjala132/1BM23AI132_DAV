#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

df = pd.read_csv('gdp.csv')

df.set_index(['country', 'year'], inplace=True)

print(df.mean())
print(df.sum())
print(df.max())
print(df.min())
print(np.mean(df['population']))
print(np.std(df['gdp']))
print(np.sum(df['life_expectency']))

df['gdp'] *= 1.10
print(df)

df_swapped = df.swaplevel('country', 'year')
df_swapped = df_swapped.sort_index(level='year')
print(df_swapped)

df_unstacked = df.unstack(level='year')
print(df_unstacked)

df = df.sort_index()
print(df)


# In[7]:


import pandas as pd
import numpy as np

df = pd.read_csv('gdp.csv') 

df.set_index(['country', 'year'], inplace=True)

print("Mean of columns:")
print(df.mean())
print()

print("Sum of columns:")
print(df.sum())
print()

print("Maximum values of columns:")
print(df.max())
print()

print("Minimum values of columns:")
print(df.min())
print()

print("Mean of 'Population' using NumPy:")
print(np.mean(df['population']))
print()

print("Standard deviation of 'GDP' using NumPy:")
print(np.std(df['gdp']))
print()

print("Sum of 'Life Expectancy' using NumPy:")
print(np.sum(df['life_expectency']))
print()

df['gdp'] *= 1.10
print("Updated DataFrame (after increasing GDP by 10%):")
print(df)
print()

df_swapped = df.swaplevel('country', 'year')
df_swapped = df_swapped.sort_index(level='year')
print("DataFrame after swapping levels and sorting by 'year':")
print(df_swapped)
print()

df_unstacked = df.unstack(level='year')
print("DataFrame after unstacking 'Year' level:")
print(df_unstacked)
print()

df_sorted = df.sort_index()
print("Final sorted DataFrame:")
print(df_sorted)


# In[ ]:





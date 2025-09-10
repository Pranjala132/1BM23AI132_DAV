#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


import pandas as pd
import numpy as np

df = pd.read_csv("place_d.csv")

mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
df['Age'] = df['Age'].astype(int)

df['City'] = df['City'].fillna("Unknown")
df = df.drop_duplicates()

df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})

def age_group(age):
    if age < 30:
        return "18-30"
    elif age < 40:
        return "30-40"
    else:
        return "40-50"

df['AgeGroup'] = df['Age'].apply(age_group)

df = pd.get_dummies(df, columns=['City'])

print(df)


# In[ ]:





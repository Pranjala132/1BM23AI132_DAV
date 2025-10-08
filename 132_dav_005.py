#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('sales_data.csv')  
pivot_revenue = df.pivot_table(values='Revenue', index='Date', columns='Salesperson', aggfunc='sum', fill_value=0)
print("Pivoted Total Revenue by Salesperson and Date:")
print(pivot_revenue)

average_revenue_per_sale = df.groupby('Product')['Revenue'].mean()
print("\nAverage Revenue per Sale for Each Product:")
print(average_revenue_per_sale)

max_units_sold = df.groupby('Salesperson')['Units Sold'].max()
print("\nMaximum Units Sold in a Single Transaction by Each Salesperson:")
print(max_units_sold)

total_revenue = df['Revenue'].sum()
revenue_by_region = df.groupby('Region')['Revenue'].sum()
revenue_percentage = (revenue_by_region / total_revenue) * 100
print("\nPercentage of Total Revenue Contributed by Each Region:")
print(revenue_percentage)

salesperson_transaction_count = df.groupby('Salesperson')['Date'].nunique()
most_sales_transactions = salesperson_transaction_count.idxmax()
print("\nSalesperson with the Most Sales Transactions:")
print(most_sales_transactions)

pivot_sales_units = df.pivot_table(values=['Revenue', 'Units Sold'], index='Salesperson', columns='Product', aggfunc='sum', fill_value=0)
print("\nPivoted Total Revenue and Units Sold by Salesperson and Product:")
print(pivot_sales_units)

pivot_units_region = df.pivot_table(values='Units Sold', index='Date', columns='Region', aggfunc='sum', fill_value=0)
print("\nPivot Table for Total Units Sold by Region on Each Date:")
print(pivot_units_region)


# In[ ]:





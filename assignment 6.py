import pandas as pd
import numpy as np
# Step 1: Read the excel file
df = pd.read_excel(r"C:\Users\HP\Downloads\array.xlsx")
print(df)

print("First five records only:")
print(df.head())

print("Last five records only:")
print(df.tail())


print("\nMissing values:")
print(df.isnull())

df.duplicated()

duplicate_count=df.duplicated().sum()
print("\nDuplicate records:", duplicate_count)

df = df.drop_duplicates()
print(df)

print("\nAfter preprocessing:")
print(df)

print("\nFinal dataset information:")
print(df.info())
print(df.isnull().sum())

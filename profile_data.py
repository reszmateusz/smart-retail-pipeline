import pandas as pd
print ("Loading data...")
df_sales = pd.read_csv("sales.csv")

print("\n1. Data preview")
print(df_sales.head())

print("\n2. Data types")
print(df_sales.info())

print("\n3. Missing values")
print(df_sales.isnull().sum())

print("\n4. Summary statistics")
print(df_sales.describe())

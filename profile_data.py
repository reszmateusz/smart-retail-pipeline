import pandas as pd
print ("wczytywanie danych")
df_sales = pd.read_csv("sales.csv")

print("\n1. Jak wyglądają dane?")
print(df_sales.head())

print("\n2. Jakie mamy typy danych?")
print(df_sales.info())

print("\n3. Czy mamy braki w danych?")
print(df_sales.isnull().sum())

print("\n4. Statysyka")
print(df_sales.describe())

import pandas as pd
df_sales = pd.read_csv("sales.csv")
df_sales['date'] = pd.to_datetime(df_sales['date'])
print(df_sales.info())

rows_before = len(df_sales)
df_sales = df_sales.drop_duplicates()
rows_after = len(df_sales)
if rows_before == rows_after:
    print("No duplicates found!")
else:
    print(f"Removed {rows_before - rows_after} duplicated rows.")
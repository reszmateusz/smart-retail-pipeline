import pandas as pd
df_sales = pd.read_csv("sales.csv")
df_sales['date'] = pd.to_datetime(df_sales['date'])
print(df_sales.info())

wiersze_przed = len(df_sales)
df_sales = df_sales.drop_duplicates()
wiersze_po = len(df_sales)
if wiersze_przed == wiersze_po:
    print("Brak dupliklatów!")
else:
    print(f"usunięto {wiersze_przed - wiersze_po} zduplikowanych wierszy")
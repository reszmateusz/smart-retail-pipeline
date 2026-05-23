import pandas as pd
import sqlite3
print("Starting load phase")

conn = sqlite3.connect('smart_retail.db')

print("Loading csv files")
df_products = pd.read_csv('products.csv')
df_inventory = pd.read_csv('inventory.csv')
df_sales = pd.read_csv('sales.csv')

print("Cleaning data and converting formats")
df_sales['date'] = pd.to_datetime(df_sales['date'])
df_sales = df_sales.drop_duplicates()

print("Pushing data to sql databases")
df_products.to_sql('products', conn, if_exists='append', index=False)
df_inventory.to_sql('inventory', conn, if_exists='append', index=False)
df_sales.to_sql('sales', conn, if_exists='append', index=False)

conn.close()

print("Success, data loaded into db successfully.")
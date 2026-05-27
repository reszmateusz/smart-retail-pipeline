import sqlite3
import pandas as pd
print("Starting data analysis")

conn = sqlite3.connect('smart_retail.db')

query_revenue = "Select Sum(total_amount) as total_revenue From sales;"
df_revenue = pd.read_sql_query(query_revenue, conn)
revenue_val = df_revenue.iloc[0,0]
print(f"\n1. Total revenue: {revenue_val}")

print("\n2. Top 3 best-selling products:")
query_top_products = """
select p.product_name, SUM(s.quantity) as total_sold, SUM(s.total_amount) as revenue
from sales s
join products p ON s.product_id = p.product_id
group by p.product_name
order by total_sold desc
limit 3;
"""
df_top = pd.read_sql_query(query_top_products, conn)
df_top.index += 1
print(df_top)

print("\n3. Low stock alerts")
query_inventory = """
select p.product_name, i.stock_quantity, i.reorder_level
from inventory i
join products p ON i.product_id = p.product_id
where i.stock_quantity <= i.reorder_level
limit 3;
"""
df_inventory = pd.read_sql_query(query_inventory, conn)
df_inventory.index += 1
print(df_inventory)

conn.close()
print("\n Analysis Complete")
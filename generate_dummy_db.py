import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta 

fake = Faker()
Faker.seed(42)
random.seed(42)

base_products = [
    {"name": "Laptop Pro", "category": "Laptopy", "price": 4500.00},
    {"name": "Laptop Basic", "category": "Laptopy", "price": 2200.00},
    {"name": "Smartfon X", "category": "Telefony", "price": 3200.00},
    {"name": "Smarfton Y", "category": "Telefony", "price": 1200.00},
    {"name": "Słuchawki bezprzewodowe", "category": "Słuchawki", "price": 450.00},
    {"name": "Głośnik bluetooth", "category": "Głośniki", "price": 200.00},
    {"name": "Myszka gamingowa", "category": "Akcesoria", "price": 180.00},
    {"name": "Klawiatura mechaniczna", "category": "Akcesoria", "price": 350.00},
    {"name": "Monitor gamingowy 27cali", "category": "Monitory", "price": 1100.00},
    {"name": "Kabel USB-C", "category": "Laptopy", "price": 35.00}
    ]

print("Generowanie tabeli Products...")
products_data = []
for i, prod in enumerate(base_products, start=1):
        products_data.append({
                "product_id": i,
                "product_name": prod["name"],
                "category": prod["category"],
                "base_price":prod["price"]
        })
df_products = pd.DataFrame(products_data)
df_products.to_csv("products.csv", index=False)

print("Generowanie tabeli Inventory...")
inventory_data = []
for i in range(1, len(base_products) + 1):
        inventory_data.append({
                "product_id": i,
                "stock_quantity": random.randint(10, 200),
                "reorder_level": random.randint(15, 50)       
        })
df_inventory = pd.DataFrame(inventory_data)
df_inventory.to_csv("Inventory.csv", index=False)

print("Generowanie tabeli Sales (10 000 transakcji z ostatnich 6 miesięcy)...")
sales_data = []
end_date = datetime.now()
start_date = end_date - timedelta(days=180)

for transaction_id in range(1, 10001):
        product_id = random.randint(1, len(base_products))
        qty = random.randint(1, 4)

        price_per_unit = products_data[product_id - 1]["base_price"]
        total_price = qty * price_per_unit

        sales_data.append({
                "transaction_id": transaction_id,
                "date": fake.date_time_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d %H:%M:%S"),
                "product_id": product_id,
                "quantity": qty,
                "total_amount": total_price
        })
df_sales = pd.DataFrame(sales_data)
df_sales = df_sales.sort_values(by="date").reset_index(drop=True)
df_sales.to_csv("sales.csv", index=False)

print("Gotowe! Wygenerowano pliki: products.csv, inventory.csv,")
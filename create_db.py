import sqlite3
print("Creating data base")

conn = sqlite3.connect('smart_retail.db')
cursor = conn.cursor()
print("Creating products table")
cursor.execute('''
Create table if not exists products (
               product_id integer primary key,
               product_name text,
               category text,
               base_price real
)
''')
print ('Creting inventory table')
cursor.execute('''
Create table if not exists inventory(
               product_id integer primary key,
               stock_quantity integer,
               reorder_level integer,
               foreign key (product_id) references products (product_id)
)
''')
print('Creating sales table')
cursor.execute('''
               create table if not exists sales (
               transaction_id integer primary key,
               date datetime,
               product_id integer,
               quantity integer,
               total_amount real,
               foreign key (product_id) references products (product_id)
)
''')

conn.commit()
conn.close()

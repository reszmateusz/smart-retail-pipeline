# Smart Retail Pipeline

A complete Data Engineering ETL pipeline built with Python and SQLite.

## 📌 Project Overview

This project simulates a data pipeline for a retail company. It extracts raw data (products, inventory, sales), transforms it by cleaning and formatting, and loads it into a relational database for further analysis.

## 🛠️ Technologies Used

- **Python** (Pandas, Faker)
- **SQLite** (Relational Database)
- **Git/GitHub** (Version Control)

## 🚀 ETL Process

1. **Extract:** Generates synthetic business data (`products.csv`, `inventory.csv`, `sales.csv`) using the `Faker` library.
2. **Transform:** Profiles the data, removes duplicates, and standardizes formats using `pandas`.
3. **Load:** Designs a relational database schema and loads the clean data into `smart_retail.db` using SQL constraints (Primary and Foreign Keys).

## 💻 How to Run (Local Setup)

1. Clone this repository.
2. Create a virtual environment and install dependencies:
   `pip install -r requirements.txt`
3. Generate the raw data files:
   `python generate_dummy_db.py`
4. Create the database and load data:
   `python create_db.py`
   `python load_data.py`

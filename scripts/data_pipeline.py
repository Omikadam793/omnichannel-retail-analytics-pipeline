import pandas as pd
import numpy as np
import sqlite3
import os

print("🚀 Starting End-to-End Retail Data Pipeline...")

# 1. Extraction: Load the core master dataset
raw_data_path = "ecommerce_sales_data.csv"
if not os.path.exists(raw_data_path):
    raise FileNotFoundError(f"Missing master data! Ensure {raw_data_path} is in the root directory.")

df = pd.read_csv(raw_data_path)
print(f"|-- Successfully extracted {len(df)} raw records.")

# 2. Transformation Layer: Data Cleaning & Standardization
# Drop any completely corrupted or unidentifiable order references
df.dropna(subset=['Order_ID'], inplace=True)

# Standardize product categories and trim whitespace noise
df['Product_Category'] = df['Product_Category'].str.strip().str.title()
df['Customer_Segment'] = df['Customer_Segment'].str.strip()

# Impute missing numeric attributes safely
df['Sales_Revenue'] = pd.to_numeric(df['Sales_Revenue'], errors='coerce').fillna(0.0)
df['Net_Profit'] = pd.to_numeric(df['Net_Profit'], errors='coerce').fillna(0.0)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(1).astype(int)

# Engineer a critical business column flag using NumPy (Day 3 check!)
df['High_Value_Transaction'] = np.where(df['Sales_Revenue'] > 1000, 'Yes', 'No')
print("|-- Transformation & cleaning sequence complete.")

# 3. Loading Layer: Push to SQL Storage (SQLite Database)
# We spin up a local SQLite instance acting as our local Data Warehouse
db_connection = sqlite3.connect("retail_data_warehouse.db")
cursor = db_connection.cursor()

# Write the clean DataFrame down to a structured SQL table
df.to_table_name = "fct_sales"
df.to_sql(df.to_table_name, con=db_connection, if_exists="replace", index=False)
print(f"|-- Success! Loaded cleaned structured data into database table: '{df.to_table_name}'")

# Export a clean backup CSV mirror for our Power BI dashboard connection
df.to_csv("data/clean_transactions.csv", index=False)
db_connection.close()
print("🎉 Pipeline executed cleanly. Target assets generated successfully.")
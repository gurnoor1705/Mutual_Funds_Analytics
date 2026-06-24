import sqlite3
import pandas as pd

print("=" * 60)
print("CREATING SQLITE DATABASE")
print("=" * 60)

connection = sqlite3.connect("mutual_funds.db")

print("Database created successfully!")

nav_history = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
nav_history.to_sql(
    "nav_history",
    connection,
    if_exists="replace",
    index=False
)
print("nav_history table created successfully!")

investor_transactions = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

investor_transactions.to_sql(
    "investor_transactions",
    connection,
    if_exists="replace",
    index=False
)

print("investor_transactions table created successfully!")

scheme_performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

scheme_performance.to_sql(
    "scheme_performance",
    connection,
    if_exists="replace",
    index=False
)

print("scheme_performance table created successfully!")

cursor = connection.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

tables = cursor.fetchall()

print("\nTables in Database:")

for table in tables:
    print(table[0])
    
connection.close()

print("Connection closed.")
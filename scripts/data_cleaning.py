import pandas as pd
import numpy as np
print("=" * 60)
print("Mutual Funds Cleaning Started")
print("=" * 60)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")
investor_transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
scheme_performance = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nNAV History Shape:", nav_history.shape)
print("Investor Transactions Shape:", investor_transactions.shape)
print("Scheme Performance Shape:", scheme_performance.shape)

print("\nConverting date column to datetime...")

nav_history["date"] = pd.to_datetime(
    nav_history["date"],
    errors="coerce"
)

print("\nData Types:")
print(nav_history.dtypes)

print("\nInvalid Dates:")
print(nav_history["date"].isna().sum())

print("\nSorting NAV History...")

nav_history = nav_history.sort_values(
    by=["amfi_code", "date"]
)

print("\nFirst 5 Records After Sorting:")
print(nav_history.head())

print("\n" + "=" * 60)
print("CHECKING MISSING NAV VALUES")
print("=" * 60)

missing_nav = nav_history["nav"].isnull().sum()

print(f"Missing NAV Values: {missing_nav}")
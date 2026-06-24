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

print("\n" + "=" * 60)
print("CHECKING DUPLICATE RECORDS")
print("=" * 60)

duplicate_count = nav_history.duplicated().sum()

print(f"Duplicate Records: {duplicate_count}")

print("\n" + "=" * 60)
print("VALIDATING NAV VALUES")
print("=" * 60)

invalid_nav = (nav_history["nav"] <= 0).sum()

print(f"Invalid NAV Values (<= 0): {invalid_nav}")

print("\n" + "=" * 60)
print("INVESTOR TRANSACTIONS - MISSING VALUE ANALYSIS")
print("=" * 60)

print(investor_transactions.isnull().sum())

print("\n" + "=" * 60)
print("CONVERTING TRANSACTION DATE")
print("=" * 60)

investor_transactions["transaction_date"] = pd.to_datetime(
    investor_transactions["transaction_date"],
    errors="coerce"
)

print("\nTransaction Data Types:")
print(investor_transactions.dtypes)

print("\nInvalid Transaction Dates:")
print(investor_transactions["transaction_date"].isna().sum())

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE - MISSING VALUE ANALYSIS")
print("=" * 60)

print(scheme_performance.isnull().sum())

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE - DUPLICATE ANALYSIS")
print("=" * 60)

duplicate_scheme = scheme_performance.duplicated().sum()

print(f"Duplicate Records: {duplicate_scheme}")

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE - RETURN VALIDATION")
print("=" * 60)

print(scheme_performance.describe())

print("\n" + "=" * 60)
print("SAVING CLEANED DATASETS")
print("=" * 60)

nav_history.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

investor_transactions.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

scheme_performance.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Cleaned datasets saved successfully!")
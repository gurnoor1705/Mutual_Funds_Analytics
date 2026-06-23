import os
import pandas as pd

print("=" * 50)
print("Mutual Fund Data Ingestion Started...")
print("=" * 50)

raw_path = "data/raw"
csv_files = [file for file in os.listdir(raw_path) if file.endswith(".csv")]

print("\nLoading datasets...\n")

for file in csv_files:

    print("=" * 60)
    print(f"Dataset: {file}")
    print("=" * 60)

    file_path = os.path.join(raw_path, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
    
    print("\nColumn Names:")
    print(df.columns.tolist())
    
    print("\n" + "=" * 60 + "\n")
    
print("\n")
print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())
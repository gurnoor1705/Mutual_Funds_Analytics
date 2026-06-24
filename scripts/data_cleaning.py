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
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

aum_by_fund_house = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

monthly_sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

category_inflows = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

industry_folio_count = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

portfolio_holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

benchmark_indices = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

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
print("UNIQUE TRANSACTION TYPES")
print("=" * 60)

print(investor_transactions["transaction_type"].unique())

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

print("\n" + "=" * 60)
print("VALIDATING TRANSACTION AMOUNTS")
print("=" * 60)

invalid_amounts = (investor_transactions["amount_inr"] <= 0).sum()

print(f"Invalid Transaction Amounts (<=0): {invalid_amounts}")

if invalid_amounts > 0:
    print(investor_transactions[investor_transactions["amount_inr"] <= 0].head())
    
print("\n" + "=" * 60)
print("KYC STATUS ENUM VALIDATION")
print("=" * 60)

print("Unique KYC Status Values:")
print(investor_transactions["kyc_status"].unique())

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = investor_transactions[
    ~investor_transactions["kyc_status"].isin(valid_kyc)
]

print(f"\nInvalid KYC Records: {len(invalid_kyc)}")

if len(invalid_kyc) > 0:
    print(invalid_kyc[["investor_id", "kyc_status"]].head())
    
    print("\n" + "=" * 60)
print("RETURN COLUMN DATA TYPES")
print("=" * 60)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

print(scheme_performance[return_columns].dtypes)

print("\n" + "=" * 60)
print("RETURN ANOMALY CHECK")
print("=" * 60)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:

    anomalies = scheme_performance[
        (scheme_performance[col] < -100) |
        (scheme_performance[col] > 100)
    ]

    print(f"{col}: {len(anomalies)} anomalies")
    
    print("\n" + "=" * 60)
print("EXPENSE RATIO VALIDATION")
print("=" * 60)

invalid_expense = scheme_performance[
    (scheme_performance["expense_ratio_pct"] < 0.1) |
    (scheme_performance["expense_ratio_pct"] > 2.5)
]

print(f"Invalid Expense Ratio Records: {len(invalid_expense)}")

if len(invalid_expense) > 0:
    print(invalid_expense[["scheme_name", "expense_ratio_pct"]])
    
print("\n" + "=" * 60)
print("REMAINING DATASET VALIDATION")
print("=" * 60)

remaining_files = {
    "fund_master": "data/raw/01_fund_master.csv",
    "aum_by_fund_house": "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": "data/raw/05_category_inflows.csv",
    "industry_folio_count": "data/raw/06_industry_folio_count.csv",
    "portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

cleaned_datasets = {}

for name, path in remaining_files.items():

    df = pd.read_csv(path)

    print(f"\n{name}")
    print(f"Shape: {df.shape}")
    print(f"Missing Values: {df.isnull().sum().sum()}")
    print(f"Duplicate Records: {df.duplicated().sum()}")

    cleaned_datasets[name] = df
    
print("\n" + "=" * 60)
print("MONTHLY SIP INFLOWS - MISSING VALUE DETAILS")
print("=" * 60)

monthly_sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(monthly_sip.isnull().sum())

print("\nRows with Missing Values:\n")

print(monthly_sip[monthly_sip.isnull().any(axis=1)])

print("\n" + "=" * 60)
print("YOY GROWTH VALIDATION")
print("=" * 60)

print(
    "Observation: 12 missing YoY values belong to the first year "
    "(2022) and are expected because previous-year data is unavailable."
)

fund_master.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

nav_history.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

aum_by_fund_house.to_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv",
    index=False
)

monthly_sip.to_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

category_inflows.to_csv(
    "data/processed/05_category_inflows_cleaned.csv",
    index=False
)

industry_folio_count.to_csv(
    "data/processed/06_industry_folio_count_cleaned.csv",
    index=False
)

scheme_performance.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

investor_transactions.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

portfolio_holdings.to_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv",
    index=False
)

benchmark_indices.to_csv(
    "data/processed/10_benchmark_indices_cleaned.csv",
    index=False
)

print("\nAll 10 cleaned datasets saved successfully!")
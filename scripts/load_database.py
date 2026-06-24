from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Database created successfully!")

# Load cleaned datasets

dim_fund = pd.read_csv("data/processed/01_fund_master_cleaned.csv")
fact_nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
fact_aum = pd.read_csv("data/processed/03_aum_by_fund_house_cleaned.csv")
fact_performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")
fact_transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

# Load into SQLite

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

fact_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

fact_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")
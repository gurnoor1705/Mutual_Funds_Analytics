from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_performance",
    "fact_transactions"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as total FROM {table}",
        engine
    )

    print(table)
    print(count)
    print()
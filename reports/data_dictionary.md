# Mutual Funds Analytics - Data Dictionary

## Project Overview
End-to-end Mutual Fund Analytics pipeline built using Python, Pandas, SQLite and SQL.

## Features

- Data Ingestion
- Live NAV Fetch using MFAPI
- Data Cleaning & Validation
- SQLite Star Schema
- Analytical SQL Queries
- Data Dictionary

## Tech Stack

- Python
- Pandas
- SQLAlchemy
- SQLite
- Git & GitHub

## Folder Structure

data/
reports/
scripts/
sql/

## Deliverables

- 10 Cleaned CSVs
- SQLite Database
- Schema Design
- SQL Queries
- Data Dictionary


## dim_fund

| Column | Data Type | Description |
|----------|------------|-------------------------------------------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct/Regular plan |
| risk_grade | TEXT | Risk classification |

---

## fact_nav

| Column | Data Type | Description |
|----------|------------|-------------------------------------------|
| amfi_code | INTEGER | AMFI scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Data Type | Description |
|----------|------------|-------------------------------------------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | AMFI scheme code |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income (Lakhs) |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

## fact_performance

| Column | Data Type | Description |
|----------|------------|-------------------------------------------|
| amfi_code | INTEGER | AMFI scheme code |
| return_1yr_pct | REAL | 1-Year return (%) |
| return_3yr_pct | REAL | 3-Year return (%) |
| return_5yr_pct | REAL | 5-Year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Alpha metric |
| beta | REAL | Beta metric |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown (%) |
| expense_ratio_pct | REAL | Expense ratio (%) |
| morningstar_rating | INTEGER | Morningstar rating |

---

## fact_aum

| Column | Data Type | Description |
|----------|------------|-------------------------------------------|
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| aum_crore | REAL | Assets Under Management (Crores) |
| market_share_pct | REAL | Market share percentage |
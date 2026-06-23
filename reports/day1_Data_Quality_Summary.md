# Day 1 Data Quality Summary

## Project
Mutual Fund Analytics Capstone

## Datasets Loaded

| Dataset | Shape |
|-----------|-----------|
| 01_fund_master | (40, 15) |
| 02_nav_history | (46000, 3) |
| 03_aum_by_fund_house | (90, 5) |
| 04_monthly_sip_inflows | (48, 6) |
| 05_category_inflows | (144, 3) |
| 06_industry_folio_count | (21, 6) |
| 07_scheme_performance | (40, 19) |
| 08_investor_transactions | (32778, 13) |
| 09_portfolio_holdings | (322, 8) |
| 10_benchmark_indices | (8050, 3) |

---

## Missing Values

Only one missing value pattern was identified:

- `04_monthly_sip_inflows.csv`
  - `yoy_growth_pct` → 12 missing values

This is expected because the initial months do not have a previous year's data for YoY calculation.

---

## Duplicate Records

No duplicate records were found in any dataset.

---

## Fund Master Exploration

### Fund Houses
10 unique fund houses

### Categories
- Equity
- Debt

### Sub Categories
12 unique sub-categories

### Risk Categories
- Low
- Moderate
- Moderately High
- High
- Very High

---

## API Integration

Successfully fetched live NAV data using mfapi.in.

Generated live NAV CSVs for:

- HDFC Top100 Direct
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

---

## AMFI Code Validation

Result:

Missing AMFI Codes:
set()

Total Missing Codes:
0

All AMFI codes in `fund_master.csv` are present in `nav_history.csv`.

---

## Overall Assessment

- All datasets loaded successfully.
- No duplicate records detected.
- Dataset quality is excellent.
- Ready for preprocessing, SQL modeling, exploratory analysis, and dashboard development.
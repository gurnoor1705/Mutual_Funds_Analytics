# 📊 Mutual Funds Analytics

An end-to-end Mutual Fund Analytics project built using **Python, Pandas, SQLite, SQLAlchemy, and SQL**. The project demonstrates a complete data engineering and analytics pipeline, including data ingestion, cleaning, validation, database design, and analytical querying.

---

## 🚀 Project Overview

This project processes multiple mutual fund datasets, performs data quality checks, generates cleaned datasets, stores them in a SQLite star schema, and enables business insights through SQL queries.

The workflow follows a typical ETL (Extract, Transform, Load) pipeline used in data analytics projects.

---

## ✨ Features

- 📥 Data Ingestion from multiple CSV sources
- 📈 Live Mutual Fund NAV fetching using MFAPI
- 🧹 Data Cleaning & Validation
- ✅ Missing value, duplicate, and anomaly detection
- 🗄 SQLite Star Schema Design
- 📊 Analytical SQL Queries
- 📚 Data Dictionary & Documentation
- 🔄 Automated ETL workflow using Python

---

## 🛠 Tech Stack

| Technology | Purpose |
|-------------|----------------------------|
| Python | Data Processing |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Operations |
| SQLite | Database Storage |
| SQLAlchemy | Database Integration |
| SQL | Analytics Queries |
| Git & GitHub | Version Control |

---

## 📁 Project Structure

```
Mutual_Funds_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│   ├── day1_Data_Quality_Summary.md
│   └── data_dictionary.md
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── data_cleaning.py
│   ├── load_database.py
│   └── verify_database.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── bluestock_mf.db
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 ETL Workflow

```
Raw CSV Files
        │
        ▼
Data Ingestion
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Processed CSV Files
        │
        ▼
SQLite Database
        │
        ▼
Star Schema Design
        │
        ▼
Analytical SQL Queries
        │
        ▼
Business Insights
```

---

## 📂 Datasets Used

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

## 🧹 Data Quality Checks Performed

### NAV History
- Date parsing and standardization
- Sorting by AMFI code and date
- Duplicate validation
- Missing value validation
- NAV > 0 validation

### Investor Transactions
- Transaction type validation
- Amount validation
- Date format standardization
- KYC status validation

### Scheme Performance
- Return data type validation
- Return anomaly detection
- Expense ratio validation

---

## 🗄 Database Design

The project follows a **Star Schema** consisting of:

### Dimension Tables

- dim_fund
- dim_date

### Fact Tables

- fact_nav
- fact_transactions
- fact_performance
- fact_aum

---

## 📊 Sample Analytical Queries

- Top 5 Funds by AUM
- Average NAV per Month
- Transactions by State
- Top Performing Funds
- Average Expense Ratio by Fund House
- Risk Grade Distribution
- Transaction Type Analysis
- Highest Sharpe Ratio Funds
- Expense Ratio < 1%
- SIP Growth Analysis

---

## 📈 Project Deliverables

- ✅ 10 Cleaned CSV Files
- ✅ SQLite Database
- ✅ Star Schema Design
- ✅ SQL Query Collection
- ✅ Data Dictionary
- ✅ Data Validation Reports

---

## 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

- Data Cleaning & Validation
- ETL Pipeline Development
- SQLite Database Design
- Star Schema Modeling
- SQL Analytics
- Data Documentation
- Git & GitHub Workflow
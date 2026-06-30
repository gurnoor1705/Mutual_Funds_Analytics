-- Top 5 Funds by AUM
SELECT
    fund_house,
    category,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average Nav per Month
SELECT
    SUBSTR(date,1,7) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- Average SIP YoY Growth
SELECT
    ROUND(AVG(yoy_growth_pct),2) AS average_yoy_growth
FROM monthly_sip_inflows;

-- Transactions by state 
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Funds with expense ratio <1%
SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Top 5 funds by Sharpe ratio
SELECT
    amfi_code,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Average expense ratio by fund house
SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Transaction count by type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

-- Highest 1-year return funds
SELECT
    d.fund_house,
    ROUND(AVG(f.expense_ratio_pct),2) AS average_expense_ratio
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code = d.amfi_code
GROUP BY d.fund_house
ORDER BY average_expense_ratio;

-- Risk grade distribution
SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_grade
ORDER BY total_funds DESC;
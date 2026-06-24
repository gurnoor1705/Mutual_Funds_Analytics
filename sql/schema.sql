-- =====================================================
-- Dimension Table : dim_fund
-- =====================================================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    risk_grade TEXT

);
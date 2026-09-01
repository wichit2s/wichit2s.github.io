-- wk09_demo.sql : ETL/ELT Demo (PostgreSQL + DuckDB / Snowflake variants)
-- 1) ELT: Load raw then transform in warehouse

-- Bronze: raw landing (no cleaning)
CREATE TABLE bronze_orders (
  order_id INT,
  customer_email TEXT,
  full_name TEXT,
  address TEXT,
  order_amount TEXT, -- keep as TEXT to preserve dirty
  order_date TEXT,
  status TEXT
);
-- \copy bronze_orders FROM 'wk09_orders_raw.csv' CSV HEADER

-- Silver: cleaned + conformed
CREATE TABLE silver_dim_customer AS
SELECT
  ROW_NUMBER() OVER (ORDER BY LOWER(TRIM(customer_email))) + 1000 AS customer_key,
  LOWER(TRIM(customer_email)) AS email,
  INITCAP(TRIM(full_name)) AS full_name,
  REGEXP_REPLACE(address, '.*(Bangkok).*', '\1') AS city,
  SUBSTRING(address FROM '([0-9]{5})') AS postcode
FROM (SELECT DISTINCT customer_email, full_name, address FROM bronze_orders) s;

CREATE TABLE silver_fact_orders AS
SELECT
  CAST(o.order_id AS INT) AS order_id,
  c.customer_key,
  CAST(NULLIF(TRIM(o.order_amount),'') AS NUMERIC) AS amount,
  CAST(o.order_date AS DATE) AS order_date,
  UPPER(TRIM(o.status)) AS status_clean
FROM bronze_orders o
LEFT JOIN silver_dim_customer c ON LOWER(TRIM(o.customer_email))=c.email
WHERE NULLIF(TRIM(o.order_amount),'') IS NOT NULL;

-- Gold: business-ready (Medallion Gold)
CREATE TABLE gold_monthly_revenue AS
SELECT date_trunc('month', order_date)::date AS month,
       SUM(amount) AS revenue,
       COUNT(*) AS order_cnt
FROM silver_fact_orders
WHERE status_clean IN ('SHIPPED','NEW','PENDING')
GROUP BY 1 ORDER BY 1;

-- 2) CDC example (incremental load by order_id watermark)
-- SELECT MAX(order_id) AS watermark FROM gold_monthly_revenue; -- store in control table
-- Then: SELECT * FROM bronze_orders WHERE order_id > :watermark

-- 3) Agentic check: schema drift handling (pseudo)
-- Python: if set(bronze_orders.columns) != set(expected): call LLM to generate ALTER TABLE

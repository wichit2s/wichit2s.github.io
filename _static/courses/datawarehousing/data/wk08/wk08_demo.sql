-- wk08_demo.sql : Physical Design Demo (PostgreSQL 15+)
-- Run with: psql -f wk08_demo.sql
-- Files: wk08_dim_product.csv, wk08_dim_customer.csv, wk08_dim_date.csv, wk08_fact_sales.csv

DROP TABLE IF EXISTS fact_sales CASCADE;
DROP TABLE IF EXISTS dim_product CASCADE;
DROP TABLE IF EXISTS dim_customer CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;

CREATE TABLE dim_product (
  product_key INT PRIMARY KEY,
  sku TEXT NOT NULL,
  product_name TEXT NOT NULL,
  category TEXT NOT NULL,
  brand TEXT NOT NULL,
  unit_price NUMERIC(10,2) NOT NULL
);

CREATE TABLE dim_customer (
  customer_key INT PRIMARY KEY,
  customer_name TEXT NOT NULL,
  region TEXT NOT NULL,
  tier TEXT NOT NULL
);

CREATE TABLE dim_date (
  date_key INT PRIMARY KEY,
  full_date DATE NOT NULL,
  year INT NOT NULL,
  month INT NOT NULL,
  week INT NOT NULL,
  day INT NOT NULL,
  weekday TEXT NOT NULL
);

-- Copy from CSV (adjust path)
\copy dim_product FROM 'wk08_dim_product.csv' CSV HEADER
\copy dim_customer FROM 'wk08_dim_customer.csv' CSV HEADER
\copy dim_date FROM 'wk08_dim_date.csv' CSV HEADER

-- ===== Unpartitioned fact (baseline) =====
CREATE TABLE fact_sales (
  sale_id INT PRIMARY KEY,
  date_key INT NOT NULL REFERENCES dim_date(date_key),
  product_key INT NOT NULL REFERENCES dim_product(product_key),
  customer_key INT NOT NULL REFERENCES dim_customer(customer_key),
  quantity INT NOT NULL,
  amount NUMERIC(12,2) NOT NULL
);

\copy fact_sales FROM 'wk08_fact_sales.csv' CSV HEADER

-- ===== Partitioned fact (range by date_key -> month) =====
CREATE TABLE fact_sales_part (
  sale_id INT NOT NULL,
  date_key INT NOT NULL,
  product_key INT NOT NULL,
  customer_key INT NOT NULL,
  quantity INT NOT NULL,
  amount NUMERIC(12,2) NOT NULL,
  PRIMARY KEY (sale_id, date_key)
) PARTITION BY RANGE (date_key);

-- Create 24 monthly partitions (2023-01 .. 2024-12) : each month ~30 days
-- date_key 1 = 2023-01-01, 31 = 2023-01-31, etc.
-- Example: 8 quarterly partitions
CREATE TABLE fact_sales_part_q1 PARTITION OF fact_sales_part FOR VALUES FROM (1) TO (92);
CREATE TABLE fact_sales_part_q2 PARTITION OF fact_sales_part FOR VALUES FROM (92) TO (183);
CREATE TABLE fact_sales_part_q3 PARTITION OF fact_sales_part FOR VALUES FROM (183) TO (274);
CREATE TABLE fact_sales_part_q4 PARTITION OF fact_sales_part FOR VALUES FROM (274) TO (365);
CREATE TABLE fact_sales_part_q5 PARTITION OF fact_sales_part FOR VALUES FROM (365) TO (456);
CREATE TABLE fact_sales_part_q6 PARTITION OF fact_sales_part FOR VALUES FROM (456) TO (547);
CREATE TABLE fact_sales_part_q7 PARTITION OF fact_sales_part FOR VALUES FROM (547) TO (638);
CREATE TABLE fact_sales_part_q8 PARTITION OF fact_sales_part FOR VALUES FROM (638) TO (729);

INSERT INTO fact_sales_part SELECT * FROM fact_sales;

-- ===== Index examples =====
-- 1) B-Tree on high-cardinality FKs (default in Postgres)
CREATE INDEX idx_fact_sales_product ON fact_sales(product_key);
CREATE INDEX idx_fact_sales_customer ON fact_sales(customer_key);
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);
-- Composite covering index for common star-join filter
CREATE INDEX idx_fact_sales_cover ON fact_sales(date_key, product_key) INCLUDE (amount, quantity);

-- For partitioned table: indexes are per-partition (local)
CREATE INDEX idx_fact_part_product ON fact_sales_part(product_key);
CREATE INDEX idx_fact_part_date ON fact_sales_part(date_key);

-- 2) BRIN for very large append-only fact (tiny index, block ranges)
CREATE INDEX idx_fact_sales_brin ON fact_sales USING BRIN (date_key) WITH (pages_per_range=128);

-- ===== EXPLAIN demo =====
-- Before index: Seq Scan
-- Run ANALYZE first
ANALYZE dim_product; ANALYZE dim_customer; ANALYZE dim_date; ANALYZE fact_sales;

-- Q1: Monthly revenue by category (star join)
EXPLAIN (ANALYZE, BUFFERS)
SELECT d.year, d.month, p.category, SUM(f.amount) AS revenue
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_product p ON f.product_key = p.product_key
WHERE d.year = 2024 AND p.category = 'Electronics'
GROUP BY d.year, d.month, p.category
ORDER BY d.year, d.month;

-- Q2: Partition pruning demo (should scan only 1 partition)
EXPLAIN (ANALYZE, BUFFERS)
SELECT SUM(amount) FROM fact_sales_part WHERE date_key BETWEEN 400 AND 430;

-- Q3: Index-only scan with covering index
EXPLAIN (ANALYZE, BUFFERS)
SELECT date_key, product_key, amount FROM fact_sales WHERE date_key = 100 AND product_key = 42;

-- ===== Maintenance =====
-- Check index size / bloat
SELECT relname, pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes WHERE relname LIKE 'idx_fact%';

-- Partition attach/detach for archiving
-- ALTER TABLE fact_sales_part DETACH PARTITION fact_sales_part_q1;

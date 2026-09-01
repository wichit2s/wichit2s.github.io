# wk09_etl_demo.py : Copy-paste runnable ETL demo (Python + DuckDB)
# pip install duckdb pandas
import duckdb, pandas as pd
con = duckdb.connect()
# Load Bronze
con.execute("CREATE TABLE bronze_orders AS SELECT * FROM read_csv('wk09_orders_raw.csv', header=True)")
print(con.execute("SELECT COUNT(*) FROM bronze_orders").fetchall())
# Transform in SQL (ELT)
con.execute("""
CREATE TABLE silver_fact_orders AS
SELECT CAST(order_id AS INT) AS order_id,
       LOWER(TRIM(customer_email)) AS email,
       CAST(NULLIF(TRIM(order_amount),'') AS DOUBLE) AS amount,
       CAST(order_date AS DATE) AS order_date,
       UPPER(TRIM(status)) AS status
FROM bronze_orders
WHERE TRIM(order_amount) <> ''
""")
print(con.execute("SELECT status, COUNT(*) FROM silver_fact_orders GROUP BY 1").fetchall())
# Data quality check (Great Expectations style)
dq = con.execute("SELECT COUNT(*) AS null_amount FROM silver_fact_orders WHERE amount IS NULL").fetchone()
print("null_amount:", dq)
# Gold
con.execute("""
CREATE TABLE gold_monthly AS
SELECT date_trunc('month', order_date)::DATE AS month, SUM(amount) AS revenue
FROM silver_fact_orders GROUP BY 1 ORDER BY 1
""")
print(con.execute("SELECT * FROM gold_monthly LIMIT 5").fetchall())

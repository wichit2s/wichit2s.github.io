-- healthinfo schema — DuckDB (embedded, columnar/analytics)
-- Usage:  duckdb healthinfo.duckdb < healthinfo_schema_duckdb.sql
--         duckdb healthinfo.duckdb < healthinfo_seed.sql
--
-- ENGINE NOTE: DuckDB enforces every declared FOREIGN KEY unconditionally and
-- gives you no switch to defer/disable checks. The shared seed intentionally
-- contains one orphan prescription (patient_id=99999) for the week-7 joins
-- lesson, so here patient_id is a *logical* reference (unconstrained). The
-- week-7 lab still shows how to declare REFERENCES in SQLite/PostgreSQL.
CREATE TABLE patients(
  patient_id   INTEGER PRIMARY KEY,
  hn           VARCHAR UNIQUE NOT NULL,
  gender       VARCHAR CHECK(gender IN ('ชาย','หญิง')),
  birth_date   VARCHAR,
  systolic_bp  DOUBLE CHECK(systolic_bp > 0),
  hba1c        DOUBLE
);

CREATE TABLE prescriptions(
  rx_id        INTEGER PRIMARY KEY,
  patient_id   INTEGER NOT NULL,  -- logical FK → patients(patient_id), not enforced
  drug         VARCHAR NOT NULL,
  dose_mg      DOUBLE,
  rx_date      VARCHAR,
  cost_thb     DOUBLE
);

CREATE TABLE referrals(rx_from INTEGER, rx_to INTEGER);

CREATE TABLE diagnoses(
  dx_id        INTEGER PRIMARY KEY,
  patient_id   INTEGER NOT NULL REFERENCES patients(patient_id),
  icd10        VARCHAR NOT NULL,
  dx_name      VARCHAR,
  dx_date      VARCHAR
);

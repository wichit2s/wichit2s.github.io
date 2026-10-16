-- healthinfo schema — PostgreSQL 14+ (client/server RDBMS)
-- Usage:  createdb healthinfo
--         psql -d healthinfo -f healthinfo_schema_postgres.sql
--         psql -d healthinfo -f healthinfo_seed.sql
--
-- This schema keeps plain INTEGER primary keys so the shared
-- healthinfo_seed.sql loads unchanged on every engine. In production
-- PostgreSQL you would normally use an identity column, e.g.:
--   patient_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
-- and insert with  ... OVERRIDING SYSTEM VALUE ...  (or omit the id).

CREATE TABLE patients(
  patient_id   INTEGER PRIMARY KEY,
  hn           TEXT UNIQUE NOT NULL,
  gender       TEXT CHECK(gender IN ('ชาย','หญิง')),
  birth_date   TEXT,
  systolic_bp  DOUBLE PRECISION CHECK(systolic_bp > 0),
  hba1c        DOUBLE PRECISION
);

-- ENGINE NOTE: the shared seed intentionally contains one orphan
-- prescription (patient_id=99999) for the week-7 joins lesson, so here
-- patient_id is a *logical* reference (unconstrained), matching
-- healthinfo_schema_duckdb.sql. diagnoses.patient_id stays enforced
-- (its seed has no orphans). The week-7 lab still shows how to declare
-- REFERENCES in SQLite/PostgreSQL.
CREATE TABLE prescriptions(
  rx_id        INTEGER PRIMARY KEY,
  patient_id   INTEGER NOT NULL,  -- logical FK → patients(patient_id), not enforced
  drug         TEXT NOT NULL,
  dose_mg      DOUBLE PRECISION,
  rx_date      TEXT,
  cost_thb     DOUBLE PRECISION
);

CREATE TABLE referrals(rx_from INTEGER, rx_to INTEGER);

CREATE TABLE diagnoses(
  dx_id        INTEGER PRIMARY KEY,
  patient_id   INTEGER NOT NULL REFERENCES patients(patient_id),
  icd10        TEXT NOT NULL,
  dx_name      TEXT,
  dx_date      TEXT
);

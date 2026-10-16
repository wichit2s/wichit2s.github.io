-- healthinfo schema — SQLite (embedded, single-file)
-- Usage:  sqlite3 healthinfo.db < healthinfo_schema_sqlite.sql
--         sqlite3 healthinfo.db < healthinfo_seed.sql
--
-- SQLite does NOT enforce FOREIGN KEY by default; that lets the shared seed
-- carry one intentional orphan prescription (patient_id=99999) used by the
-- week-7 joins lesson. Enable per connection when you want enforcement:
--   PRAGMA foreign_keys = ON;

CREATE TABLE patients(
  patient_id   INTEGER PRIMARY KEY,
  hn           TEXT UNIQUE NOT NULL,
  gender       TEXT CHECK(gender IN ('ชาย','หญิง')),
  birth_date   TEXT,
  systolic_bp  REAL CHECK(systolic_bp > 0),
  hba1c        REAL
);

CREATE TABLE prescriptions(
  rx_id        INTEGER PRIMARY KEY,
  patient_id   INTEGER NOT NULL REFERENCES patients(patient_id),
  drug         TEXT NOT NULL,
  dose_mg      REAL,
  rx_date      TEXT,
  cost_thb     REAL
);

CREATE TABLE referrals(rx_from INTEGER, rx_to INTEGER);

CREATE TABLE diagnoses(
  dx_id        INTEGER PRIMARY KEY,
  patient_id   INTEGER NOT NULL REFERENCES patients(patient_id),
  icd10        TEXT NOT NULL,
  dx_name      TEXT,
  dx_date      TEXT
);

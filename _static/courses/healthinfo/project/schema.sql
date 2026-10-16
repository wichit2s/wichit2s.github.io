-- 1. บังคับใช้ Foreign Key Constraint ใน SQLite
PRAGMA foreign_keys = ON;

-- 2. สร้างตารางประชากรผู้ป่วย (patients)
CREATE TABLE IF NOT EXISTS patients (
    patient_id_hash TEXT PRIMARY KEY,
    age_group TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('M', 'F'))
);

-- 3. สร้างตารางสัญญาณชีพและผลแล็บ (vitals_labs) พร้อม Domain Constraints
CREATE TABLE IF NOT EXISTS vitals_labs (
    lab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id_hash TEXT NOT NULL,
    sbp REAL CHECK(sbp BETWEEN 50 AND 300),
    hba1c REAL CHECK(hba1c BETWEEN 3.0 AND 20.0),
    lab_date TEXT NOT NULL,
    FOREIGN KEY (patient_id_hash) REFERENCES patients(patient_id_hash) ON DELETE CASCADE
);

-- 4. สร้างตารางประวัติการสั่งจ่ายยา (prescriptions)
CREATE TABLE IF NOT EXISTS prescriptions (
    rx_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id_hash TEXT NOT NULL,
    drug_name TEXT NOT NULL,
    rx_date TEXT NOT NULL,
    FOREIGN KEY (patient_id_hash) REFERENCES patients(patient_id_hash) ON DELETE CASCADE
);

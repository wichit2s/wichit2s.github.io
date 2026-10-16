import sqlite3
import pandas as pd

conn = sqlite3.connect('health_cdss.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

with open('schema.sql', 'r', encoding='utf-8') as f:
    cursor.executescript(f.read())

df = pd.read_csv('deidentified_patients_hour2.csv')

df_patients = df[['patient_id_hash', 'age_group', 'gender']].drop_duplicates()
df_patients.to_sql('patients', conn, if_exists='append', index=False)

df_vitals = df[['patient_id_hash', 'sbp', 'hba1c', 'admittime']].copy()
df_vitals.rename(columns={'admittime': 'lab_date'}, inplace=True)
df_vitals.dropna(subset=['lab_date'], inplace=True)
df_vitals.to_sql('vitals_labs', conn, if_exists='append', index=False)

df_rx = df[df['sbp'] >= 140][['patient_id_hash', 'admittime']].copy()
df_rx['drug_name'] = 'Amlodipine 5mg'
df_rx.rename(columns={'admittime': 'rx_date'}, inplace=True)
df_rx.dropna(subset=['rx_date'], inplace=True)
df_rx.to_sql('prescriptions', conn, if_exists='append', index=False)

conn.commit()
conn.close()
print("✅ สร้างและย้ายข้อมูลลงฐานข้อมูล health_cdss.db สำเร็จเรียบร้อยแล้ว!")

import sqlite3
import pandas as pd

conn = sqlite3.connect('health_cdss.db')

cdss_query = """
WITH LatestVitals AS (
    SELECT 
        patient_id_hash, sbp, hba1c, lab_date,
        ROW_NUMBER() OVER (PARTITION BY patient_id_hash ORDER BY lab_date DESC) as rn
    FROM vitals_labs
)
SELECT 
    v.patient_id_hash,
    p.age_group,
    p.gender,
    v.sbp,
    v.hba1c,
    v.lab_date,
    CASE 
        WHEN v.sbp >= 180 OR v.hba1c >= 9.0 THEN 'CRITICAL'
        WHEN v.sbp >= 140 OR v.hba1c >= 7.0 THEN 'HIGH'
        ELSE 'MODERATE'
    END AS risk_tier
FROM LatestVitals v
JOIN patients p ON v.patient_id_hash = p.patient_id_hash
WHERE v.rn = 1
  AND NOT EXISTS (
      SELECT 1 FROM prescriptions rx 
      WHERE rx.patient_id_hash = v.patient_id_hash
  )
ORDER BY v.sbp DESC;
"""

df_triage = pd.read_sql_query(cdss_query, conn)
conn.close()

df_triage.to_csv('critical_triage_report.csv', index=False)

print("🚨 รายงานผู้ป่วยกลุ่มวิกฤตขาดการรับยา (Care Gap Triage Queue):")
print(df_triage.head(5))
print(f"\n✅ ส่งออกไฟล์ critical_triage_report.csv เรียบร้อยแล้ว (จำนวน {len(df_triage)} ราย)")

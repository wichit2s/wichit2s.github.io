SELECT 
    v.patient_id_hash,
    v.sbp,
    v.hba1c,
    v.lab_date
FROM vitals_labs v
WHERE v.sbp >= 180
  AND NOT EXISTS (
      SELECT 1 
      FROM prescriptions p
      WHERE p.patient_id_hash = v.patient_id_hash
  );

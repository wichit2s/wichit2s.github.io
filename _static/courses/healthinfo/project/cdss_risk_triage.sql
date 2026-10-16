SELECT 
    patient_id_hash,
    sbp,
    hba1c,
    lab_date,
    CASE
        WHEN sbp >= 180 OR hba1c >= 9.0 THEN 'CRITICAL'
        WHEN sbp >= 140 OR hba1c >= 7.0 THEN 'HIGH'
        WHEN sbp >= 120 OR hba1c >= 5.7 THEN 'MODERATE'
        ELSE 'NORMAL'
    END AS risk_tier
FROM vitals_labs
ORDER BY sbp DESC;

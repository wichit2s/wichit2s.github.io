WITH RankedVitals AS (
    SELECT 
        patient_id_hash,
        sbp,
        hba1c,
        lab_date,
        ROW_NUMBER() OVER (
            PARTITION BY patient_id_hash 
            ORDER BY lab_date DESC
        ) AS rn
    FROM vitals_labs
)
SELECT 
    patient_id_hash,
    sbp,
    hba1c,
    lab_date AS latest_visit_date
FROM RankedVitals
WHERE rn = 1;

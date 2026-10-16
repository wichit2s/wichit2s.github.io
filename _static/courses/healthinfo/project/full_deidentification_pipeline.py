import pandas as pd
import hashlib

df = pd.read_csv('cleaned_patients_hour1.csv')

SALT = "AMMS302_SECRET_SALT_KEY_2026"
def hash_patient_id(patient_id):
    return hashlib.sha256((SALT + str(patient_id)).encode('utf-8')).hexdigest()[:16]

df['patient_id_hash'] = df['patient_id'].apply(hash_patient_id)

def bin_age(age):
    if age >= 90:
        return '90+'
    group_start = (int(age) // 10) * 10
    return f"{group_start}-{group_start+9}"

df['age_group'] = df['age'].apply(bin_age)

df_deidentified = df.drop(columns=['patient_id', 'patient_name', 'national_id', 'age'], errors='ignore')

df_deidentified.to_csv('deidentified_patients_hour2.csv', index=False)
print("✅ สร้างไฟล์ deidentified_patients_hour2.csv เรียบร้อยแล้ว!")

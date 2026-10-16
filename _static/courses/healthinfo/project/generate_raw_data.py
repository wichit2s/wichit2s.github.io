import pandas as pd
import random
from datetime import datetime, timedelta
import os

# อ่านรายชื่อจังหวัดจากไฟล์ thai_demographics.csv
demo_path = 'thai_demographics.csv'
if not os.path.exists(demo_path) and os.path.exists('/workspace/artifacts/thai_demographics.csv'):
    demo_path = '/workspace/artifacts/thai_demographics.csv'

if os.path.exists(demo_path):
    df_demo = pd.read_csv(demo_path)
    provinces = df_demo['city'].tolist()
else:
    provinces = ['อำนาจเจริญ', 'กรุงเทพมหานคร', 'อุบลราชธานี', 'ขอนแก่น', 'เชียงใหม่']

random.seed(42)
data = []

for i in range(1, 1001):
    admit = datetime(2026, 1, 1) + timedelta(days=random.randint(1, 180))
    disch = admit + timedelta(days=random.randint(-2, 14)) # จำลองตรรกะเวลาผิดพลาด
    
    data.append({
        'patient_id': f'HN-{i:05d}',
        'patient_name': f'Patient_{i}',
        'national_id': f'13499{i:08d}',
        'province': random.choice(provinces),
        'age': random.choice([25, 45, 62, 78, 92, 105]), # Age > 89 Outliers
        'gender': random.choice(['M', 'F']),
        'sbp': random.choice([115, 128, 142, 185, 350, None]),
        'hba1c': random.choice([5.4, 6.2, 7.8, 11.2, None]),
        'admittime': admit.strftime('%Y-%m-%d %H:%M:%S'),
        'dischtime': disch.strftime('%Y-%m-%d %H:%M:%S')
    })

df_raw = pd.DataFrame(data)
df_raw.to_csv('raw_patients.csv', index=False)
print("✅ บันทึก raw_patients.csv สำเร็จ (พร้อมคอลัมน์ province ไทย)!")

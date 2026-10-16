import pandas as pd

df = pd.read_csv('raw_patients.csv')
df['admittime'] = pd.to_datetime(df['admittime'])
df['dischtime'] = pd.to_datetime(df['dischtime'])
df['los_days'] = (df['dischtime'] - df['admittime']).dt.total_seconds() / 86400

df_valid = df[(df['los_days'] >= 0) & ((df['sbp'].isnull()) | (df['sbp'].between(50, 300)))].copy()

Q1 = df_valid['sbp'].quantile(0.25)
Q3 = df_valid['sbp'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

iqr_mask = (df_valid['sbp'].isnull()) | ((df_valid['sbp'] >= lower_bound) & (df_valid['sbp'] <= upper_bound))
df_cleaned = df_valid[iqr_mask].copy()

df_cleaned['admittime'] = df_cleaned['admittime'].dt.strftime('%Y-%m-%d %H:%M:%S')
df_cleaned['dischtime'] = df_cleaned['dischtime'].dt.strftime('%Y-%m-%d %H:%M:%S')
df_cleaned.drop(columns=['los_days'], inplace=True, errors='ignore')

df_cleaned.to_csv('cleaned_patients_hour1.csv', index=False)
print(f"ขอบเขต IQR ของ SBP: [{lower_bound:.1f}, {upper_bound:.1f}] mmHg")
print(f"✅ บันทึกไฟล์ cleaned_patients_hour1.csv เรียบร้อยแล้ว (คงเหลือ {len(df_cleaned)} แถว)")

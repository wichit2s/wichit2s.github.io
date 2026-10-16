import pandas as pd

df = pd.read_csv('raw_patients.csv')

df['admittime'] = pd.to_datetime(df['admittime'])
df['dischtime'] = pd.to_datetime(df['dischtime'])

df['los_days'] = (df['dischtime'] - df['admittime']).dt.total_seconds() / 86400

valid_time_mask = df['los_days'] >= 0
df_time_clean = df[valid_time_mask].copy()

valid_vitals_mask = (df_time_clean['sbp'].isnull()) | (df_time_clean['sbp'].between(50, 300))
df_valid = df_time_clean[valid_vitals_mask].copy()

print(f"จำนานแถวเดิม: {len(df)} ➔ หลังตรวจตรรกะเวลาและค่าเป็นไปไม่ได้: {len(df_valid)}")

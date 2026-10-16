import pandas as pd

df = pd.read_csv('raw_patients.csv')

print(f"มิติชุดข้อมูล (Rows, Cols): {df.shape}")
print("\n--- สรุปชนิดข้อมูล (df.info()) ---")
df.info()

print("\n--- สรุปจำนวนค่าว่าง (isnull().sum()) ---")
print(df.isnull().sum())

print("\n--- สถิติสรุปภาพรวม (df.describe()) ---")
print(df[['age', 'sbp', 'hba1c']].describe())

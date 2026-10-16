import pandas as pd

# โหลดไฟล์ประชากรไทย thai_demographics.csv สำหรับ PySynthea
try:
    from synthea import Generator, GeneratorOptions
    options = GeneratorOptions()
    options.population_size = 1000
    options.seed = 42
    options.demographics_file = "thai_demographics.csv"
    options.state = "Thailand"
    options.city = "อำนาจเจริญ"

    generator = Generator(options)
    cohort = generator.run()
    df_raw = cohort.to_dataframe(table="patients")
    df_raw.to_csv('raw_patients.csv', index=False)
    print("✅ บันทึก raw_patients.csv สำเร็จโดยใช้ PySynthea + thai_demographics.csv!")
except Exception as e:
    print(f"PySynthea fallback mode: {e}")
    import generate_raw_data

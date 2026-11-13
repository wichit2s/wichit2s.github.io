การทำคลังข้อมูล
====================================

.. warning::

   ฉบับปรับปรุงเน้นการใช้งานในยุค Generative AI

จุดมุ่งหมาย
------------------------------------------------------------

1. นักศึกษาสามารถอธิบายหลักการทำคลังข้อมูลและการแทนความรู้จากการทำคลังข้อมูล
2. นักศึกษาสามารถอธิบายขั้นตอนวิธีในการพัฒนาและออกแบบโมเดลข้อมูลในการทำคลังข้อมูล
3. นักศึกษาสามารถใช้ซอฟต์แวร์ในการเก็บรักษาข้อมูลและแยกข้อมูล
4. นักศึกษาสามารถอธิบายวิธีการทำคลังข้อมูลด้วยเทคการแปลงข้อมูลและโหลดข้อมูล 


คำอธิบายรายวิชา
------------------------------------------------------------

  แนวคิดเกี่ยวกับคลังข้อมูล ความหมาย โครงสร้าง กระบวนการจัดการ การพัฒนาโมเดลข้อมูล การออกแบบโมเดลข้อมูล กระบวนการในการเก็บรักษาข้อมูล การแยกข้อมูล การแปลงข้อมูลและการโหลดข้อมูล ประสิทธิภาพการออกแบบโมเดลข้อมูล กรณีศึกษาทางธุรกิจ


  Concepts of data warehousing; definition, structures, management process; data model development; data model design; data retention process; data extraction; data conversion and data loading; data design performance; business case study


แผนการเรียนรู้
------------------------------------------------------------

.. list-table:: แผนการสอนรายวิชา Modern Data Warehousing for Generative AI
   :header-rows: 1
   :widths: 4 10 12 12

   * - สัปดาห์
     - หัวข้อ
     - ผลลัพธ์การเรียนรู้
     - ลิงก์สื่อการเรียนรู้เพิ่มเติม

   * - 1
     - บทนำสู่ Data Warehousing ยุคใหม่
     - เข้าใจภาพรวมของ Modern DW และความเชื่อมโยงกับ Generative AI
     - https://www.snowflake.com/guides/what-is-data-warehouse

   * - 2
     - Architectures
     - วิเคราะห์และเปรียบเทียบสถาปัตยกรรม DW สมัยใหม่
     - https://docs.databricks.com/lakehouse/index.html

   * - 3
     - Data Modeling สำหรับ DW
     - ออกแบบโมเดลข้อมูล Star และ Snowflake ได้อย่างเหมาะสม
     - https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/

   * - 4
     - Data Ingestion & ETL/ELT
     - วางแผนและพัฒนา pipeline สำหรับ ingest ข้อมูล
     - https://docs.getdbt.com/docs/introduction

   * - 5
     - Data Quality & Governance
     - ประเมินคุณภาพข้อมูลและนำหลัก Data Governance ไปประยุกต์
     - https://greatexpectations.io/

   * - 6
     - Modern Storage Formats
     - เลือกใช้ format เช่น Parquet/Delta/Iceberg ให้เหมาะกับ use-case
     - https://delta.io/

   * - 7
     - SQL for Analytics & Feature Engineering
     - เขียน SQL เชิงลึกเพื่อวิเคราะห์และสร้างฟีเจอร์สำหรับ AI
     - https://mode.com/sql-tutorial/

   * - 8
     - Midterm: Hands-on Project Review
     - นำเสนอ pipeline ที่ออกแบบเอง และได้รับ feedback
     - (ไฟล์แนบ/รายงานตามที่อาจารย์กำหนด)

   * - 9
     - Introduction to Generative AI
     - อธิบายการทำงานของ LLM และแนวคิดพื้นฐานของ GenAI
     - https://platform.openai.com/docs/introduction

   * - 10
     - Connecting DW to GenAI
     - สร้าง flow ในการนำข้อมูลจาก DW ไปใช้ใน GenAI
     - https://docs.langchain.com/

   * - 11
     - RAG (Retrieval Augmented Generation)
     - สร้างระบบที่ใช้ข้อมูลจาก DW เพื่อ enhance LLM
     - https://www.llamaindex.ai/

   * - 12
     - DW สำหรับ Fine-tuning
     - เตรียม dataset สำหรับ fine-tune LLM ด้วยข้อมูลจาก DW
     - https://huggingface.co/docs/transformers/training

   * - 13
     - Case Study: Chatbot/AI Generator
     - ออกแบบระบบ AI ที่ใช้ DW จริงในการตอบคำถาม
     - https://cloud.google.com/solutions/genai-chat-app-data

   * - 14
     - Final Project Work
     - สร้างโครงงานแบบ end-to-end ที่บูรณาการเนื้อหาทั้งหมด
     - (Google Colab / GitHub / เอกสารแนบตามกลุ่ม)

   * - 15
     - Final Presentation
     - นำเสนอผลงานสรุป และอภิปรายศักยภาพของระบบที่สร้าง
     - (ไฟล์สไลด์ / สรุปผลการนำเสนอ)

เกณฑ์การให้คะแนนรายวิชา
--------------------------

.. list-table:: สัดส่วนคะแนน
   :widths: 50 10 40
   :header-rows: 1

   * - รายการ
     - สัดส่วน (%)
     - หมายเหตุ
   * - การบ้าน

       **ประกอบด้วย**

       1. แบบฝึกหัดรายสัปดาห์ / Quizzes
       2. แบบฝึกหัดเขียน SQL/ETL/Modeling
       3. การมีปฏิสัมพันธ์ ถาม-ตอบ ช่วยเหลือเพื่อน ฯลฯ
     - 30%
     - * ตรวจสอบความเข้าใจรายบท
       * ทักษะทางเทคนิค
   * - ประเมินรายงาน / โครงงาน

       **เกณฑ์ย่อย**

       1. ออกแบบ schema ได้ถูกต้อง สอดคล้องกับ use-case
       2. ใช้ข้อมูลจาก DW ใน pipeline ของ GenAI เช่น RAG
       3. ใช้ Snowflake, dbt, LangChain ฯลฯ ได้อย่างเหมาะสม
       4. อธิบายเหตุผลและการเลือกวิธีการได้ดี
       5. อธิบายเข้าใจง่าย มี demo หรือ dashboard ประกอบ
     - 20%
     - ความสามารถในการอธิบาย วิเคราะห์ และสื่อสาร
   * - สอบกลางภาค (Midterm Examination)
     - 25%
     - เนื้อหาสัปดาห์ที่ 1 - 7
   * - สอบปลายภาค (Final Examination)
     - 25%
     - เนื้อหาสัปดาห์ที่ 8 - 15


=========================================================
Workshop in Health Informatics
=========================================================

.. meta::
   :description: Course syllabus and timetable for Workshop in Health Informatics Course
   :keywords: health informatics, data wrangling, SQL, medical data, course timetable

ปฏิบัติการสารสนเทศด้านสุขภาพ (Workshop in Health Informatics)
-----------------------------------------------------------


เป้าหมายของรายวิชา (Course Goals)
=================================
พัฒนานักศึกษาให้มีความรู้และทักษะเกี่ยวกับการเขียนโปรแกรมเพื่อจัดการข้อมูล รูปแบบข้อมูลสุขภาพประเภทต่างๆ การจัดการข้อมูลขนาดใหญ่ การทำงานกับฐานข้อมูล สามารถนำไปประยุกต์ใช้ในการทำงานทางด้านวิทยาศาสตร์การแพทย์ทั่วไปและทางด้านการแพทย์แม่นยำ โดยยึดหลักความถูกต้องตามหลักวิชาการ

ผลลัพธ์การเรียนรู้ของรายวิชา (CLOs)
==================================
เมื่อสิ้นสุดการเรียนการสอนแล้ว นักศึกษาจะสามารถ:

1. **CLO1:** อธิบายเกี่ยวกับรูปแบบข้อมูลสุขภาพประเภทต่างๆ การทำงานกับฐานข้อมูล
2. **CLO2:** เขียนโปรแกรมเพื่อจัดการข้อมูล รวมถึงการจัดการข้อมูลขนาดใหญ่
3. **CLO3:** อธิบายเกี่ยวกับกฎหมายและจริยธรรมที่เกี่ยวข้องกับการจัดการข้อมูล
4. **CLO4:** ใช้เทคโนโลยีสารสนเทศเพื่อการปฏิบัติงานด้านวิทยาศาสตร์การแพทย์ได้ตรงตามวัตถุประสงค์

แผนการสอนและการเรียนรู้ (Course Timetable)
=========================================

.. list-table:: แผนการสอนรายวิชา อจวพ ๓๐๒ ปฏิบัติการสารสนเทศด้านสุขภาพ
   :widths: 8 50 42
   :header-rows: 1

   * - คาบที่
     - หัวข้อ / รายละเอียด
     - วิธีการสอนและสื่อที่ใช้
   * - 1
     - **Introduction to Health Informatics Data Pre-processing**
       
       - Working with CSV, JSON
       - Data pre-processing
       - Saving intermediate work
       - Introduction to offline Jupyter Notebook
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์

       * `สไลด์ <../../_static/courses/healthinfo/wk01.html>`_
       * `pandas input/output ฟังก์ชัน <https://pandas.pydata.org/pandas-docs/stable/reference/io.html>`_

       Software

       * `scoop <https://scoop.sh>`_
       * `uv <https://docs.astral.sh/uv/>`_
       * `jupyterlab <https://jupyterlab.readthedocs.io/en/latest/>`_
   * - 2
     - **Data Linking and Aggregation**
       
       - การเชื่อมโยงข้อมูลจากหลายชุดข้อมูล
       - Group by / having
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data

       * `สไลด์ <../../_static/courses/healthinfo/wk02.html>`_
   * - 3
     - **Finding Insights with pandas**
       
       - การวิเคราะห์และค้นหาข้อมูลเชิงลึกด้วย pandas Library
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data

       * `สไลด์ <../../_static/courses/healthinfo/wk03.html>`_
   * - 4
     - **Big Data Infrastructure**
       
       - ETL process, data pipeline, data lake
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data

       * `สไลด์ <../../_static/courses/healthinfo/wk04.html>`_
   * - 5
     - **Relational Database & SQL (Part 1)**
       
       - Relational database & database schema
       - column type, SELECT statement, LIMIT
       - primary key, SQLite, SQL INSERT
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data
   * - 6
     - **Data Warehouse & SQL Queries**
       
       - Data warehouse & Basic database design
       - SQL WHERE (AND, OR, NOT, NULL)
       - AS ALIAS, ORDER BY, MIN, MAX, AVG, COUNT, DISTINCT
       - DATE, LIKE, IN, BETWEEN
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data
   * - 7
     - **Advanced Database Design & Joins**
       
       - ER diagram, FOREIGN key
       - SQL JOIN (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, SELF JOIN)
       - Dot notation, UNION, GROUP BY, HAVING
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data
   * - 8
     - **Finding Insights with SQL**
       
       - การสืบค้นและค้นหาข้อมูลสุขภาพเชิงลึกด้วยคำสั่ง SQL
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Dataset: General Practice Prescribing Data
   * - 9
     - **สอบกลางภาค**
       
       - การสอบวัดผลกลางภาคเรียน
     - การสอบปฏิบัติงาน/ทฤษฎีในชั้นเรียน
   * - 10
     - **Health Information Ethics and Regulations**
       
       - กฎหมายและจริยธรรมที่เกี่ยวข้องกับการจัดการข้อมูลสุขภาพ
       - Data privacy, security, PII
       - พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล (PDPA) และมาตรฐาน HIPAA
       - นโยบายคลาวด์กลางด้านสาธารณสุข
     - บรรยาย: PowerPoint และค้นคว้าข้อมูลเกี่ยวกับกฎหมาย PDPA, HIPAA
   * - 11
     - **Health Care Data Standards**
       
       - มาตรฐานข้อมูลสุขภาพสากล
       - OMOP Common Data Model, HL7 FHIR
       - รหัสมาตรฐานสากล ICD-10
     - บรรยาย: PowerPoint และค้นคว้าข้อมูลจาก สปสช. Data Dictionary
   * - 12
     - **Finding Insights from Big Data (Part 1)**
       
       - การใช้งานระบบ Google BigQuery
       - การวิเคราะห์ข้อมูลผู้ป่วยจำลองที่สร้างจาก Synthea (Synthetic patient data)
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Google BigQuery และ Synthea
   * - 13
     - **Finding Insights from Big Data (Part 2)**
       
       - การวิเคราะห์ข้อมูลผู้ป่วยจำลองบนรูปแบบ OMOP Common Data Model
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Synthetic Patient Data in OMOP
   * - 14
     - **Techniques when dealing with Big Data**
       
       - Big Data manipulation techniques
       - Table view, table update, and Permission management
     - บรรยาย: PowerPoint และฝึกปฏิบัติในห้องปฏิบัติการคอมพิวเตอร์ด้วย Synthetic Patient Data
   * - 15
     - **Project Consultation**
       
       - การให้คำปรึกษาโครงงานกลุ่มของนักศึกษา
       - หัวข้อ: การสร้าง ER diagram จาก สปสช. Data Dictionary
     - การทำโครงงานกลุ่มและการให้คำปรึกษาโดยอาจารย์ผู้สอน
   * - 16
     - **Project Presentation**
       
       - การนำเสนอโครงงานกลุ่มวิเคราะห์ข้อมูลสุขภาพของนักศึกษา
     - การนำเสนอผลงานกลุ่มและการอภิปรายร่วมกันในชั้นเรียน
   * - 17
     - **สอบปลายภาค**
       
       - การสอบวัดผลสัมฤทธิ์ปลายภาคเรียน
     - การสอบภาคปฏิบัติและทฤษฎีปลายภาค

การประเมินผลการเรียนรู้ (Course Evaluation)
==========================================
สัดส่วนคะแนนสะสมและการวัดผล (ร้อยละ 100) มีดังนี้:

* **การสอบทฤษฎีและปฏิบัติ (MCQ / Exams):** ร้อยละ 50
* **การส่งงานและการบ้านประจำสัปดาห์ (Homework):** ร้อยละ 20
* **โครงงานกลุ่มวิเคราะห์ข้อมูลสุขภาพ (Project):** ร้อยละ 20
* **การนำเสนอผลงานโครงงานกลุ่ม (Presentation):** ร้อยละ 10

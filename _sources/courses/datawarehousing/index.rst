========================================================================
**การสร้างคลังข้อมูล**
========================================================================

.. list-table:: กำหนดการวิชาการสร้างคลังข้อมูลและโครงการประกอบการเรียน
   :widths: 8 42 25 25
   :header-rows: 1

   * - **สัปดาห์ที่**
     - **หัวข้อและรายละเอียดกิจกรรม**
     - **กิจกรรมโครงการ (Project Phase)**
     - **แหล่งข้อมูลและลิงก์**
   * - 1

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk01.html>`_
     - **บทนำสู่ DW/BI และทบทวนฐานข้อมูล**

       ภารกิจของคลังข้อมูลเพื่อการตัดสินใจ และรูปแบบปกติที่ 3 (3NF)
     - **Phase 1:** กำหนดขอบเขตธุรกิจและรวบรวมความต้องการสำหรับ "แพลตฟอร์มอีคอมเมิร์ซอัจฉริยะ"
     - `History of Data Warehousing <https://www.geeksforgeeks.org/history-of-data-warehousing/>`_
   * - 2

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk02.html>`_
     - **ระเบียบวิธีออกแบบ**: การเปรียบเทียบแนวทางของ **Inmon** (Top-down) และ **Kimball** (Bottom-up)
     - วิเคราะห์ระบบต้นทาง (Source Systems) และเลือกวิธีออกแบบที่เหมาะสมกับโครงการ
     - `Kimball vs Inmon Models <https://en.wikipedia.org/wiki/Bill_Inmon>`_
   * - 3

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk03.html>`_
     - **Dimensional Modeling I**: การสร้าง **Star Schema**, ตารางข้อเท็จจริง (Fact) และตารางมิติ (Dimension)
     - ออกแบบ Star Schema เบื้องต้นสำหรับยอดขาย (Sales Analysis)
     - `Principles of Dimensional Modeling <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/>`_
   * - 4

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk04.html>`_
     - **Dimensional Modeling II**: การจัดการมิติที่เปลี่ยนแปลงช้า (**SCD**) และ Junk Dimensions
     - **Phase 1 (ต่อ):** ออกแบบ SCD Type 2 เพื่อติดตามประวัติลูกค้าในโครงการ
     - `SCD Management Techniques <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/slowly-changing-dimension/>`_
   * - 5

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk05.html>`_
     - **การรวบรวมความต้องการ**: การใช้ **Information Packages** เพื่อกำหนดตัวชี้วัดและลำดับชั้น (Hierarchies)
     - สรุปแผนภาพ Information Package สำหรับโครงการส่งอาจารย์
     - `The Data Warehouse Lifecycle <https://www.wiley.com/en-us/The+Data+Warehouse+Lifecycle+Toolkit%2C+2nd+Edition-p-9780470149775>`_
   * - 6

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk06.html>`_
     - **วิวัฒนาการสู่คลาวด์**: การแยกส่วน Storage และ Compute บนแพลตฟอร์มอย่าง Snowflake หรือ BigQuery
     - **Phase 2:** เริ่มต้นตั้งค่าสภาพแวดล้อมบนคลาวด์เพื่อเตรียมรับข้อมูลโครงการ
     - `Cloud DW For Dummies <https://www.itupdate.com/resource/cloud-data-warehousing-for-dummies/>`_
   * - 7

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk07.html>`_
     - **Data Lakehouse**: การใช้ **Medallion Architecture** (Bronze, Silver, Gold Layers)
     - ออกแบบการจัดเก็บข้อมูลโครงการตามเลเยอร์ Medallion
     - `Medallion Architecture Guide <https://www.databricks.com/glossary/medallion-architecture>`_
   * - 8

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk08.html>`_
     - **การออกแบบทางกายภาพ**: กลยุทธ์การทำ Indexing และ Partitioning รวมถึงการสอบกลางภาค
     - ปรับแต่งประสิทธิภาพ (Physical Tuning) ของตารางในโครงการ
     - `Physical Design Process <https://www.postgresql.org/docs/current/indexes.html>`_
   * - 9

       :icon:`fa-solid fa-link` `slides <../../_static/courses/datawarehousing/wk09.html>`_
     - **ท่อส่งข้อมูล (ETL vs. ELT)**: การเปลี่ยนผ่านสู่ ELT และการใช้ Change Data Capture (CDC)
     - **Phase 3:** สร้างท่อส่งข้อมูลจากไฟล์ Raw (Bronze) ไปยังตาราง Silver
     - `ETL vs ELT Shift <https://www.rivery.io/blog/etl-vs-elt/>`_
   * - 10
     - **คุณภาพและธรรมาภิบาล**: การทำ Data Profiling และ Master Data Management (MDM)
     - สร้างการตรวจสอบคุณภาพข้อมูล (Data Quality Checks) อัตโนมัติในท่อส่งข้อมูล
     - `OpenMetadata Context Layer <https://open-metadata.org/>`_
   * - 11
     - **เลเยอร์ความหมาย (Semantic Layer)**: การรวมตรรกะธุรกิจเพื่อให้ AI และผู้ใช้เห็นข้อมูลตรงกัน
     - พัฒนา Semantic Layer (เช่น dbt หรือ Looker) สำหรับโครงการ
     - `Semantic Layer Architecture <https://www.databricks.com/blog/semantic-layer-architecture-components-design-patterns-and-ai-integration>`_
   * - 12
     - **การวิเคราะห์หลายมิติ (OLAP)**: การทำ Slicing, Dicing และ Drilling down บนชุดข้อมูล
     - สร้างแดชบอร์ดเบื้องต้นเพื่อทดสอบการวิเคราะห์แบบ OLAP
     - `ClickHouse Developer Course <https://tinybird.co/clickhouse-course>`_
   * - 13
     - **การเพิ่มประสิทธิภาพด้วย AI**: การใช้ ML สำหรับ Query Optimization และพยากรณ์ปริมาณงาน
     - **Phase 4:** นำผลพยากรณ์จาก ML มาช่วยปรับขนาดทรัพยากรคลาวด์ในโครงการ
     - `AI-Driven DW Innovations <https://doi.org/10.37745/ejcsit.2013/vol13n52185194>`_
   * - 14
     - **AI เอเจนต์ในวิศวกรรมข้อมูล**: การสร้างท่อส่งข้อมูลที่เยียวยาตัวเองได้ (Self-healing Pipelines)
     - พัฒนา AI เอเจนต์พื้นฐานเพื่อตรวจจับข้อผิดพลาดใน Pipeline ของโครงการ
     - `Agentic AI for Data Engineering <https://doi.org/10.47059/ijirct.2024.v12i03.009>`_
   * - 15
     - **เวิร์กโฟลว์ AI ระดับการผลิต**: การใช้ **Agentic Views** และการนำเสนอโครงการสุดท้าย
     - นำเสนอ "The Agentic E-Commerce Platform" ที่สามารถตอบคำถามภาษาธรรมชาติได้
     - `AV-SQL: Agentic Views <https://arxiv.org/abs/2512.08769>`_


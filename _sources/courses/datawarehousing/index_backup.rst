การทำคลังข้อมูล
====================================

.. warning: 

   ฉบับปรับปรุงเพื่อเน้นการประยุกต์แพลตฟอร์มเพื่อรองรับการใช้งาน AI

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

.. list-table:: แผนการสอนรายสัปดาห์วิชา Data Warehousing
   :header-rows: 1
   :widths: 5 15 20 25 15

   * - สัปดาห์
     - หัวข้อหลัก
     - หัวข้อย่อย
     - วัตถุประสงค์
     - ลิงก์ประกอบ
   * - 1
     - บทนำสู่ Data Warehousing ยุค AI
     - ความแตกต่าง Data Lake / Lakehouse / DW, บทบาทของ AI
     - เข้าใจบริบทการเปลี่ยนผ่านจากคลังข้อมูลแบบดั้งเดิมสู่ AI-driven platform
     - https://databricks.com
   * - 2
     - AI-native Data Architectures
     - Lakehouse, Vector Database, Multimodal Storage
     - เข้าใจการออกแบบสถาปัตยกรรมข้อมูลที่รองรับ AI เช่น LLM/Embedding
     - https://pinecone.io
   * - 3
     - AI-ready Data Modeling
     - Feature Store, Semantic Layer, Ontologies
     - เข้าใจแนวคิดการเตรียมข้อมูลให้พร้อมสำหรับ AI Training/Inference
     - https://feast.dev
   * - 4
     - Modern ETL/ELT & Streaming
     - Data ingestion tools (Airbyte, Kafka, dbt)
     - สร้าง pipeline สำหรับ real-time และ batch data ingestion สำหรับ AI
     - https://docs.getdbt.com
   * - 5
     - Unstructured Data & Embedding Index
     - Text/Image/Audio storage, vector embedding
     - เรียนรู้การจัดการข้อมูลไม่มีโครงสร้างเพื่อให้ใช้งานกับ LLM ได้
     - https://langchain.com
   * - 6
     - Data Quality, Bias & Explainability
     - Detecting bias, profiling, data lineage
     - วิเคราะห์คุณภาพข้อมูลและผลกระทบต่อ AI ด้วย Explainable AI (XAI)
     - https://arxiv.org/pdf/2001.07588.pdf
   * - 7
     - Governance & AI Compliance
     - AI Act, Data Provenance, Auditing
     - เข้าใจข้อกำหนดด้านจริยธรรมและกฎหมายของการใช้ข้อมูลใน AI
     - https://www.europa.eu (EU AI Act)
   * - 8
     - Midterm Project Pitch
     - AI data pipeline + storage proposal
     - นำเสนอแนวคิด project ที่รวมการจัดเก็บและใช้ข้อมูลสำหรับ AI
     - https://notion.so
   * - 9
     - Foundation Models & Training Data Strategy
     - Training dataset structure, scale, diversity
     - ออกแบบคลังข้อมูลให้เหมาะสมกับ model training ในระดับ foundation
     - https://huggingface.co/docs
   * - 10
     - Retrieval-Augmented Generation (RAG)
     - Hybrid architecture, document retrieval + LLM
     - สร้าง data schema ที่สามารถใช้ร่วมกับ RAG pipeline
     - https://docs.llamaindex.ai
   * - 11
     - AI Inference & Vector Search
     - Similarity search, ANN Index, Faiss
     - สร้างคลังข้อมูลที่ใช้สำหรับ AI inference ผ่าน vector search
     - https://facebookresearch.github.io/faiss
   * - 12
     - Monitoring & Observability
     - ML observability, data drift, model feedback loop
     - ออกแบบระบบ DW ที่สามารถตรวจสอบและปรับปรุงข้อมูลให้ AI
     - https://evidentlyai.com
   * - 13
     - Synthetic Data Generation
     - Generative modeling, Data simulation, Augmentation
     - ใช้ AI สร้างข้อมูลจำลองเพื่อนำไปใช้ใน DW/AI pipeline
     - https://gretel.ai
   * - 14
     - Final Project Presentation
     - นำเสนอ DW/AI integrated solution
     - แสดงความเข้าใจภาพรวมตั้งแต่ ingestion ถึงการใช้ข้อมูลกับ AI
     - https://slidesgo.com
   * - 15
     - Reflection & Trends
     - Data mesh, decentralized AI, future outlook
     - วิเคราะห์แนวโน้มคลังข้อมูลในยุค AI และการเตรียมความพร้อมด้านอาชีพ
     - https://towardsdatascience.com



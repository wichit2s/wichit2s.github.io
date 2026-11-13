========================================================================================
โครงงานสำหรับนักศึกษาปีสอง 
========================================================================================

ข้อมูลทั่วไปของรายวิชา (Course Overview)
========================================

* **ชื่อรายวิชา:** โครงงานสำหรับนักศึกษาปีสอง (Sophomore Project)
* **จำนวนหน่วยกิต:** 3 หน่วยกิต 3(0-6-3) [บรรยาย 0 ชม. / ปฏิบัติ 6 ชม. / ศึกษาด้วยตนเอง 3 ชม. ต่อสัปดาห์]
* **คำอธิบายรายวิชา (Course Description):**

  เฟรมเวิร์คอาไจล์ เครื่องมือที่ใช้ในการทำงานร่วมกัน การพัฒนาซอฟต์แวร์แบบทีม การวางแผนโครงการ การจัดการความเสี่ยงของโครงการ การนำเสนอด้วยวาจา การฝึกปฏิบัติในหัวข้อที่เกี่ยวข้อง


  *(Agile framework; collaborative tools; team software development; project planning; project risk management; oral presentation; laboratory work in related topics)*


ตารางจัดการเรียนรู้ 
========================================================================

.. list-table:: แผนการจัดการเรียนรู้รายสัปดาห์ กรณีศึกษา Grocery Store POS Platform
   :widths: 8 30 30 32
   :header-rows: 1

   * - สัปดาห์ที่ (Week)
     - หัวข้อการเรียนรู้ 
     - ผลลัพธ์การเรียนรู้ (ชิ้นงาน)
     - เอกสารประกอบ 
   * - 1
     - **Orientation & Team Formation**

       * ปฐมนิเทศวิชาและชี้แจงกรอบ YLO2 / CLOs
       * การจัดตั้งทีม (1–3 คน) และเลือกอาจารย์ที่ปรึกษา
       * แนะนำโจทย์ตัวอย่าง: Grocery Store POS Platform
     - **LLO:** เข้าใจเป้าหมายวิชา YLO2, จัดตั้งทีม 1–3 คน และเสนออาจารย์ที่ปรึกษาได้

       **CLO:** CLO1

       ใบจัดตั้งทีมและตอบรับอาจารย์ที่ปรึกษา (Team Formation Form)
     - * `สไลด์ <../../_static/courses/project2/wk01.html>`_
       * เอกสาร มคอ.3 ฉบับเต็ม
       * DSSI YLO2 Roadmap Slide
       * POS Case Study Brief
   * - 2
     - **Project Scope & Problem Statement**

       * วิเคราะห์โจทย์ปัญหาของร้านขายของชำ (Grocery Store Pain Points)
       * กำหนดขอบเขตระบบ (Scope Boundaries: In-Scope vs Out-of-Scope)
     - **LLO:** วิเคราะห์ปัญหาธุรกิจร้านค้าชำและกำหนดขอบเขตระบบ POS 15 สัปดาห์ได้อย่างสมเหตุสมผล

       **CLO:** CLO1, CLO3

       Draft Project Charter & Proposal Document
     - * `สไลด์ <../../_static/courses/project2/wk02.html>`_
       * Problem Statement Canvas
       * Project Scope Boundary Guide
       * Charter Template
   * - 3
     - **Requirements Analysis & User Stories**

       * การเก็บรวบรวม Functional / Non-Functional Requirements
       * การจัดทำ SRS และ User Story Mapping (`As a Cashier...`)
     - **LLO:** แปลงความต้องการของเจ้าของร้าน/พนักงานเป็น SRS และ User Story Backlog ได้

       **CLO:** CLO2, CLO3

       Software Requirements Specification (SRS) & User Story Backlog
     - * `สไลด์ <../../_static/courses/project2/wk03.html>`_
       * SRS Document Template
       * Agile User Story Mapping Guide
       * Acceptance Criteria Checklist
   * - 4
     - **Agile Framework & Collaborative Tools**

       * ตั้งค่า Agile Board (GitHub Projects / Jira)
       * กำหนด Git Branching Strategy (`main`, `develop`, `feature/*`)
     - **LLO:** บริหาร Agile Board และใช้ Git Branching Strategy ในการทำงานร่วมกันเป็นทีมได้

       **CLO:** CLO1, CLO2

       Team GitHub Repository & Configured Kanban Board
     - * `สไลด์ <../../_static/courses/project2/wk04.html>`_
       * GitHub Projects Setup Guide
       * Git Flow & Branching Rules
       * Pull Request Policy
   * - 5
     - **System Architecture & Data Modeling**

       * ออกแบบ 3-Tier Architecture (Frontend, Backend, DB)
       * ออกแบบ ER Diagram, DB Schema (Products, Orders, Stock, Users)
     - **LLO:** ออกแบบสถาปัตยกรรมซอฟต์แวร์ ฐานข้อมูลเชิงสัมพันธ์ และข้อกำหนด API ได้ถูกต้อง

       **CLO:** CLO2

       System Architecture Diagram, DB Schema & API Specification
     - * `สไลด์ <../../_static/courses/project2/wk05.html>`_
       * ERD & Database Design Guide
       * OpenAPI / Swagger Specs
       * Clean Architecture Principles
   * - 6
     - **Sprint 1 Planning & Environment Setup**

       * วางแผน Sprint 1 Backlog & ประเมิน Story Points
       * จัดเตรียม Development Boilerplate & Docker Environment
     - **LLO:** วางแผน Sprint 1, ประเมินเวลา และสร้าง Project Boilerplate ที่เชื่อมต่อ DB ได้

       **CLO:** CLO1, CLO2

       Sprint 1 Backlog List & Executable Project Boilerplate
     - * `สไลด์ <../../_static/courses/project2/wk06.html>`_
       * Planning Poker Guide
       * Docker Compose Boilerplate
       * Environment Setup Manual
   * - 7
     - **Sprint 1 Development & Code Review**

       * พัฒนาฟีเจอร์หลัก (Product CRUD, Barcode Management)
       * ปฏิบัติการ Peer Code Review และ refactoring ตาม Clean Code
     - **LLO:** เขียนโค้ดระบบจัดการสินค้าตามมาตรฐาน Clean Code และปรับแก้ตาม Code Review ได้

       **CLO:** CLO1, CLO2

       Source Code Commit on GitHub & Working Increment
     - * `สไลด์ <../../_static/courses/project2/wk07.html>`_
       * Clean Code Rules for POS
       * Code Review Checklist
       * Pull Request Guide
   * - 8
     - **Midterm Progress Defense**

       * สอบนำเสนอความก้าวหน้าโครงงานต่อคณะกรรมการ
       * สาธิตระบบตัวอย่าง (Live Prototype Demo: คิดเงิน/จัดการสินค้า)
     - **LLO:** นำเสนอความก้าวหน้าเชิงเทคนิคและสาธิตระบบตัวอย่างต่อคณะกรรมการได้อย่างชัดเจน

       **CLO:** CLO4

       Midterm Defense Slide Deck & Working Prototype Demo
     - * `สไลด์ <../../_static/courses/project2/wk08.html>`_
       * Midterm Presentation Template
       * Prototype Demo Checklist
       * Scoring Rubric Guide
   * - 9
     - **Sprint 2 Planning & Advanced Development**

       * ปรับปรุง Backlog ตาม Feedback คณะกรรมการกลางภาค
       * พัฒนาหน้าจอคิดเงิน (POS Counter) & การตัดสต็อกขนาน (DB Transaction)
     - **LLO:** ปรับแก้ไขระบบตาม Feedback กลางภาค และพัฒนาฟีเจอร์คิดเงินพร้อมระบบตัดสต็อกได้

       **CLO:** CLO1, CLO2, CLO3

       Updated Product Backlog & POS Counter Source Code
     - * `สไลด์ <../../_static/courses/project2/wk09.html>`_
       * Midterm Revision Log
       * DB Transaction & Concurrency Guide
       * POS UI UX Best Practices
   * - 10
     - **System Integration & Advanced Analytics**

       * เชื่อมโยง Frontend, Backend และ Database เต็มรูปแบบ
       * พัฒนา Analytics Dashboard (DS Track) / Real-time Stock Alert (SI Track)
     - **LLO:** บูรณาการส่วนประกอบของระบบเข้าด้วยกัน และพัฒนาฟีเจอร์ระดับสูงประจำวิชาเอกได้

       **CLO:** CLO2

       Fully Integrated POS Beta Version (Live Demo URL)
     - * `สไลด์ <../../_static/courses/project2/wk10.html>`_
       * Full-Stack Integration Guide
       * Sales Analytics Dashboard Specs
       * WebSocket & Notification Tutorial
   * - 11
     - **Project Risk Review & Data Ethics (PDPA)**

       * วิเคราะห์และบริหารความเสี่ยงเชิงเทคนิคที่เกิดขึ้นจริง
       * ตรวจสอบความปลอดภัยซอฟต์แวร์ (OWASP) และมาตรฐาน PDPA
     - **LLO:** บริหารความเสี่ยงเชิงเทคนิคและตรวจสอบการคุ้มครองข้อมูลส่วนบุคคลตาม PDPA ได้

       **CLO:** CLO3

       Project Risk Mitigation Log & PDPA Compliance Report
     - * `สไลด์ <../../_static/courses/project2/wk11.html>`_
       * Risk Management Log Template
       * OWASP Top 10 Security Guide
       * Thailand PDPA Guidelines
   * - 12
     - **Software Testing & Quality Assurance (QA)**

       * เขียน Unit Test / Integration Test สำหรับระบบคิดเงินและสต็อก
       * ทดสอบ Usability Testing กับผู้ใช้จริง (เจ้าของร้าน/พนักงาน)
     - **LLO:** ดำเนินการทดสอบซอฟต์แวร์ตามหลัก QA และสรุปผล Usability Testing ได้อย่างถูกต้อง

       **CLO:** CLO2, CLO3

       Test Plan, Test Cases, Bug Tracking & Usability Test Report
     - * `สไลด์ <../../_static/courses/project2/wk12.html>`_
       * Software QA & Testing Suite Guide
       * Usability Survey Form
       * Bug Tracking Log Template
   * - 13
     - **Documentation & User Manual**

       * เรียบเรียงรายงานโครงงานฉบับสมบูรณ์ (บทที่ 1–5)
       * จัดทำคู่มือการติดตั้ง (Deployment Guide) และคู่มือผู้ใช้ (User Manual)
     - **LLO:** จัดทำเอกสารรายงานโครงงานฉบับสมบูรณ์และคู่มือการใช้งานสำหรับเจ้าของร้านได้

       **CLO:** CLO4

       Final Project Report (PDF) & POS User Manual
     - * `สไลด์ <../../_static/courses/project2/wk13.html>`_
       * TQF Report Format Template
       * User Manual Design Guide
       * APA 7th Citation Guide
   * - 14
     - **Final System Deployment & Defense Preparation**

       * ติดตั้งระบบบน Production Cloud Environment (AWS/Render/Vercel)
       * ซ้อมนำเสนอและเตรียมสไลด์การสอบป้องกันฉบับสมบูรณ์
     - **LLO:** Deploy ระบบ POS ขึ้น Production Cloud และเตรียมการนำเสนอได้อย่างเป็นมืออาชีพ

       **CLO:** CLO2, CLO4

       Deployed Live Production URL & Final Presentation Slide Deck
     - * `สไลด์ <../../_static/courses/project2/wk14.html>`_
       * Cloud Deployment Manual (Docker/PaaS)
       * Presentation Rehearsal Guide
       * Final Defense Slide Template
   * - 15
     - **Final Project Defense & Handover**

       * สอบนำเสนอและป้องกันโครงงานฉบับสมบูรณ์ต่อคณะกรรมการ
       * ตรวจรับรองความถูกต้องของระบบ และส่งมอบซอฟต์แวร์ฉบับสมบูรณ์
     - **LLO:** นำเสนอผลงานฉบับสมบูรณ์ ตอบคำถามเชิงเทคนิค และส่งมอบระบบซอฟต์แวร์ที่ใช้งานได้จริง

       **CLO:** CLO1, CLO2, CLO3, CLO4

       Final Project Deliverables Package & Verified Software Handover
     - * `สไลด์ <../../_static/courses/project2/wk15.html>`_
       * Final Defense Rubric
       * Software Handover Checklist
       * GitHub Final Release Tag



ผลลัพธ์การเรียนรู้ระดับรายวิชา
-----------------------------------------------------------------

1. **CLO1 (Agile & Teamwork):** ประยุกต์ใช้กรอบการทำงานแบบ Agile (Scrum/Kanban) และเครื่องมือทำงานร่วมกัน (Collaborative Tools/Git Workflow) ในการวางแผน แบ่งหน้าที่ และติดตามความก้าวหน้าการพัฒนาซอฟต์แวร์เป็นทีมได้อย่างมีประสิทธิภาพ *(สอดคล้องกับ PLO2, PLO4, SILO1)*
2. **CLO2 (Software Engineering & Architecture):** ออกแบบสถาปัตยกรรมซอฟต์แวร์ แบบจำลองฐานข้อมูล (Database Schema) และพัฒนาโปรแกรมประยุกต์ร่วมกันเป็นทีม ให้ถูกต้องตามหลักการวิศวกรรมซอฟต์แวร์และมาตรฐาน Clean Code *(สอดคล้องกับ PLO2, SILO1, SILO2)*
3. **CLO3 (Data Processing & Risk Management):** วิเคราะห์ รวบรวม และจัดการข้อมูลจากแหล่งที่กำหนดเพื่อสนับสนุนฟังก์ชันการทำงานของซอฟต์แวร์ พร้อมทั้งวิเคราะห์และบริหารความเสี่ยงของโครงการได้อย่างเหมาะสมและมีจริยธรรมข้อมูล *(สอดคล้องกับ PLO1, PLO5, DSLO1, DSLO2)*
4. **CLO4 (Communication & Demonstration):** นำเสนอความก้าวหน้า สาธิตการทำงานของซอฟต์แวร์ (Software Demo) ด้วยวาจา และจัดทำเอกสารรายงานโครงงานฉบับสมบูรณ์ได้อย่างถูกต้อง ชัดเจน และเป็นมืออาชีพ *(สอดคล้องกับ PLO3)*



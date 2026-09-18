การพัฒนาเว็บแอปพลิเคชันเต็มรูปแบบพื้นฐาน 
===================================================================================

**รหัสวิชา:** 1145101  

**จำนวนหน่วยกิต:** 3(2-2-5)  

วัตถุประสงค์ของรายวิชา
--------------------------
1. เข้าใจแนวคิดสถาปัตยกรรม Client-Server, โปรโตคอลการสื่อสารข้อมูลพื้นฐาน (HTTP/HTTPS) และการรักษาความปลอดภัย
2. เข้าใจและสามารถออกแบบ API ตามสถาปัตยกรรม REST (Representational State Transfer)
3. เข้าใจแนวคิดการบริหารจัดการสถานะและช่วงการใช้งาน (Status & Session Management)
4. สามารถพัฒนา Full-Stack Web Application และ RESTful API โดยใช้ Django Framework และ Django REST Framework
5. สามารถใช้งานเครื่องมือทดสอบ API ได้แก่ **HTTPie CLI** และ **HTTPie Desktop** (ติดตั้งผ่าน **Scoop**)
6. เข้าใจภาพรวมสถาปัตยกรรมระบบ (System Design Overview) และการประยุกต์ใช้ Containerization ด้วย **Podman** สำหรับการนำแอปพลิเคชันไปใช้งานจริง (Deployment Infrastructure) บนเครื่องคอมพิวเตอร์ส่วนบุคคลเพียงเครื่องเดียว

แผนการสอนรายสัปดาห์ (15 สัปดาห์)
------------------------------------

.. warning::
   เพิ่มสไลด์รายสัปดาห์

.. list-table:: แผนการสอน
   :header-rows: 1
   :widths: 5 30 45 20

   * - **สัปดาห์**
     - **หัวข้อการเรียนรู้**
     - **กิจกรรมการเรียนรู้และเครื่องมือ**
     - **การประเมินผล**
   * - 1
     - แนะนำสถาปัตยกรรม Client-Server และโปรโตคอลการสื่อสารข้อมูลพื้นฐาน
     - บรรยายสถาปัตยกรรม Client-Server, DNS, HTTP/HTTPS และ SSL/TLS

       * ฝึกใช้ Browser DevTools (Network Tab) และ cURL
       * `สไลด์ <../../_static/courses/fullstack/wk01.html>`_
     - การสังเกตพฤติกรรม
   * - 2
     - สถาปัตยกรรม REST API และเครื่องมือทดสอบ API (HTTPie)
     - บรรยายหลักการ REST, HTTP Methods และ Status Codes

       * ติดตั้ง **HTTPie CLI** และ **HTTPie Desktop** ผ่าน **Scoop** (`scoop install httpie`, `scoop install httpie-desktop`) และทดลองส่ง Request
       * `สไลด์ <../../_static/courses/fullstack/wk02.html>`_
     - แบบฝึกหัด
   * - 3
     - ภาพรวมสถาปัตยกรรมระบบ (System Design Overview - Part I)
     - บรรยายแนวคิด System Design, เปรียบเทียบ Monolithic vs Microservices

       * วาดและวิเคราะห์ System Architecture Diagram สำหรับ Web Application
       * `สไลด์ <../../_static/courses/fullstack/wk03.html>`_
     - ใบงานวิเคราะห์สถาปัตยกรรม
   * - 4
     - การเริ่มต้นพัฒนาเว็บแอปพลิเคชันด้วย Django Framework
     - บรรยายปรัชญา Batteries-Included และสถาปัตยกรรม MVT ใน Django

       * ติดตั้ง Python, Virtual Environment (`venv`) และสร้าง Django Project
       * `สไลด์ <../../_static/courses/fullstack/wk04.html>`_
     - ตรวจการตั้งค่าโปรเจกต์
   * - 5
     - การจัดการข้อมูลและการออกแบบฐานข้อมูลด้วย Django ORM
     - บรรยาย Relational Database, Normalization และ Django ORM

       * สร้าง Models, กำหนดความสัมพันธ์ (1:N, N:M), ทำ Migrations และใช้ Django Admin
       * `สไลด์ <../../_static/courses/fullstack/wk05.html>`_
     - การบ้าน
   * - 6
     - การประมวลผลฟอร์ม การจัดการ View และ Template Rendering
     - บรรยาย FBV, CBV, Django Template Language (DTL) และ Static Files

       * พัฒนาหน้าเว็บและทำระบบ CRUD ผ่าน Django Forms / ModelForms
       * `สไลด์ <../../_static/courses/fullstack/wk06.html>`_
     - แบบฝึกหัด
   * - 7
     - การบริหารจัดการสถานะและช่วงการใช้งาน (Status & Session)
     - บรรยาย Stateless Protocol, Cookies และ Sessions ใน Django

       * เขียนโค้ดจัดการ `request.session` สำหรับระบบตะกร้าสินค้า/บันทึกสถานะ
       * `สไลด์ <../../_static/courses/fullstack/wk07.html>`_
     - แบบทดสอบย่อย
   * - 8
     - โครงงานย่อย Midterm และการสอบกลางภาค
     - นำเสนอแนวคิดโครงงาน Full-Stack Web Application และสอบประเมินความรู้

       * ประเมินการออกแบบ MVT Architecture และโครงสร้างระบบ
     - โครงงานกลางภาค / สอบกลางภาค
   * - 9
     - ความปลอดภัยของเว็บแอปพลิเคชัน (Web Application Security)
     - บรรยายช่องโหว่เว็บ (XSS, CSRF, SQL Injection) และระบบ Django Authentication

       * เปิดใช้งานระบบ Login/Logout/Register และทดสอบ CSRF Protection
       * `สไลด์ <../../_static/courses/fullstack/wk09.html>`_
     - การบ้าน
   * - 10
     - การพัฒนา RESTful API ด้วย Django REST Framework (DRF)
     - บรรยายสถาปัตยกรรม DRF, Serializers, APIView และ ViewSets

       * สร้าง RESTful API Endpoints และทดสอบส่งข้อมูลด้วย **HTTPie CLI / Desktop**
       * `สไลด์ <../../_static/courses/fullstack/wk10.html>`_
     - แบบฝึกหัด
   * - 11
     - การเชื่อมต่อส่วนหน้า (Frontend Integration) และ Token-Based Authentication
     - บรรยาย Decoupled Architecture, Token/JWT Authentication และ CORS

       * ตั้งค่า `django-cors-headers` และใช้ JavaScript Fetch API เรียกใช้ DRF API
       * `สไลด์ <../../_static/courses/fullstack/wk11.html>`_
     - ใบงานปฏิบัติการ
   * - 12
     - ภาพรวมสถาปัตยกรรมระบบ (System Design Overview - Part II)
     - บรรยาย Stateless Application, Caching และการจัดการ Static/Media Files

       * ตั้งค่า Caching ใน Django และจัดโครงสร้างโปรเจกต์ตามหลัก 12-Factor App
       * `สไลด์ <../../_static/courses/fullstack/wk12.html>`_
     - การบ้าน
   * - 13
     - พื้นฐาน คอนเทนเนอร์ (Containerization) และ Podman
     - บรรยายแนวคิด Containerization, เปรียบเทียบ Podman vs Docker (Rootless & Daemonless)

       * ติดตั้ง Podman / Podman Desktop และฝึกใช้คำสั่ง CLI (`podman run`, `podman ps`, `podman images`)
       * `สไลด์ <../../_static/courses/fullstack/wk13.html>`_
     - แบบฝึกหัด
   * - 14
     - การสร้าง Container Image และ Multi-Container ด้วย Podman
     - บรรยายการเขียน `Containerfile` และการใช้งาน `podman-compose` / Podman Pods

       * สร้าง Container Image ของ Django และเชื่อมต่อกับ PostgreSQL ด้วย `podman-compose`
       * `สไลด์ <../../_static/courses/fullstack/wk14.html>`_
     - โครงงานย่อย
   * - 15
     - การนำเว็บไปใช้งานจริง (Deployment Infrastructure) และการนำเสนอผลงาน
     - บรรยาย Production Architecture (Nginx + Gunicorn + Django + PostgreSQL) บน Podman

       * จำลองการ Deploy Production Stack บนเครื่องเดี่ยว และนำเสนอโครงงานปลายภาค
       * `สไลด์ <../../_static/courses/fullstack/wk15.html>`_
     - นำเสนอปลายภาค


สัดส่วนการประเมินผล
----------------------
- การมีส่วนร่วมและพฤติกรรมในชั้นเรียน: 10%
- งานบ้านและแบบฝึกหัดปฏิบัติการ: 20%
- โครงงานกลางภาคและการสอบกลางภาค: 25%
- โครงงานปลายภาค (Full-Stack Web Application + Podman Deployment): 30%
- การนำเสนอและรายงานสรุปผลงาน: 15%

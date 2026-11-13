การพัฒนาโปรแกรมสำหรับมือถือด้วย Flutter
============================================================

.. warning::

   ฉบับปรับปรุง 1-2568

   * เพิ่มเนื้อหา GetX สำหรับจัดเการข้อมูลจำเป็นของผู้ใช้ช้

   * เพิ่มการเรียกใช้ข้อมูลผ่าน PocketBase

   * เพิ่มการเรียกใช้ LLM ผ่าน MCP server


.. list-table:: แผนการเรียนรู้ Flutter + GetX + PocketBase + MCP
   :header-rows: 1

   * - สัปดาห์
     - หัวข้อ
     - วัตถุประสงค์
     - ลิงก์ประกอบ
   * - 1
     - แนะนำ Flutter และการติดตั้ง
     - ติดตั้ง Flutter และรันแอปแรกได้
     - https://docs.flutter.dev/get-started
   * - 2
     - พื้นฐาน Widget และ Layout
     - เข้าใจ Stateless/Stateful widget และ layout
     - https://docs.flutter.dev/development/ui/widgets
   * - 3
     - Navigation และ Routing
     - สร้าง navigation และส่งข้อมูลระหว่างหน้า
     - https://docs.flutter.dev/development/ui/navigation
   * - 4
     - Forms และ Input
     - ใช้ TextField, Form, และ validation เบื้องต้น
     - https://docs.flutter.dev/cookbook/forms/validation
   * - 5
     - การจัดการ State พื้นฐาน
     - ใช้ setState และแนวคิด reactive programming
     - https://docs.flutter.dev/development/data-and-backend/state-mgmt/intro
   * - 6
     - พื้นฐานการเชื่อมต่อ API
     - ดึงข้อมูลจาก REST API ด้วย http package
     - https://docs.flutter.dev/cookbook/networking/fetch-data
   * - 7
     - สรุปก่อนสอบ
     - ทบทวนเนื้อหาและเตรียมสอบกลางภาค
     - -
   * - 8
     - สอบกลางภาค
     - ประเมินความเข้าใจพื้นฐาน Flutter
     - -
   * - 11
     - ทบทวนเนื้อหาก่อนกลางภาค

       * `สไลด์ <../../_static/courses/mobiledev/wk11.html>`_
     - Flutter Review & Compass Application
     - https://docs.flutter.dev/app-architecture/case-study
   * - 12
     - การพัฒนา Backend

       * `สไลด์ <../../_static/courses/mobiledev/wk12.html>`_
     - REST API Backend with Django REST Framework, JWT Authentication & OAuth2/OpenID Connect Server (Lab: django-oidc-provider + Flutter Web)
     - https://www.django-rest-framework.org/

       https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

       https://django-oidc-provider.readthedocs.io/en/latest/

       https://pub.dev/packages/openid_client
   * - 13
     - การพัฒนา Flutter Data Layer

       * `สไลด์ <../../_static/courses/mobiledev/wk13.html>`_
     - Data Layer (Services & Repositories)
     -
   * - 14
     - การพัฒนา Flutter UI Layer

       * `สไลด์ <../../_static/courses/mobiledev/wk14.html>`_
     - UI Layer (ViewModels, Views & Command Pattern)
     -
   * - 15
     - Dependency Injection & Testing

       * `สไลด์ <../../_static/courses/mobiledev/wk15.html>`_
     - การพึ่งพากันผ่านระบบและการทดสอบ
     -
   * - 16
     - นำเสนอโปรเจกต์

       * `สไลด์ <../../_static/courses/mobiledev/wk16.html>`_
     - Course Project: real mobile app on branch ``project`` + README + video demo (OIDC authentication, main functions & extra features)
     - เกณฑ์การให้คะแนน (Rubric) อยู่ในสไลด์

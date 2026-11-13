การพัฒนาเว็บ
============================================================

.. warning::

  เอกสารชุดนี้อยู่ในระหว่างการปรับปรุง

.. list-table:: แผนการจัดการเรียนรู้
   :widths: 5 55 40
   :header-rows: 1

   * - สัปดาห์ที่ 
     - สาระการเรียนรู้
     - เอกสารประกอบ
   * - 1 
     - ความรู้เบื้องต้นเกี่ยวกับการพัฒนาเว็บ 

       **ผลลัพธ์การเรียนรู้**

       1. เข้าใจองค์ประกอบสำคัญของการพัฒนาเว็บ (Frontend+Backend+Storage)
       2. แสดงรายการเทคโนโลยี Frontend ได้อย่างน้อย 3 รายการ
       3. แสดงรายการเทคโนโลยี Backend ได้อย่างน้อย 3 รายการ
       4. แสดงรายการ Storage ได้อย่างน้อย 3 รายการ
       5. ติดตั้งโปรแกรมที่จำเป็นสำหรับการพัฒนาเว็บด้วย django ได้
       
       .. collapse:: แบบฝึกหัดภาคทฤษฏี

         1. อธิบายองค์ประกอบของระบบการพัฒนาเว็บว่าเกี่ยวข้องกับส่วนใดบ้าง พร้อมยกตัวอย่างแต่ละส่วน
         2. จงระบุเทคโนโลยีที่ใช้ในฝั่ง Frontend อย่างน้อย 3 รายการ พร้อมอธิบายหน้าที่ของแต่ละรายการ
         3. จงระบุเทคโนโลยีที่ใช้ในฝั่ง Backend อย่างน้อย 3 รายการ พร้อมอธิบายสั้น ๆ ว่าแต่ละตัวทำงานอย่างไร 
         4. จงระบุระบบจัดเก็บข้อมูลอย่างน้อย 3 รายการ พร้อมระบุว่าระบบใดเป็นแบบ SQL และแบบ NoSQL

       .. collapse:: แบบฝึกหัดภาคปฏิบัติ

         1. แสดงการติดตั้ง Python และ Django ในเครื่องของตัวเอง
         2. แสดงคำสั่งที่ใช้ในการติดตั้ง
         3. สร้างโปรเจกต์ชื่อ mysite และเปิดการใช้งานให้สำเร็จ

     - 1. `Chapter 1 Web Applications <https://www.softkraft.co/web-application-architecture/>`_
       2. `Web Development <https://www.geeksforgeeks.org/web-development/>`_
       3. `การติดตั้ง <https://www.slideshare.net/slideshow/python-dev-setup-thaipdf/253351612>`_ 

          * `scoop <https://scoop.sh/>`_
           - git
           - anaconda3
          * `สมัครใช้ pycharm professional <https://www.jetbrains.com/shop/eform/students>`_
          * `download pycharm professional <https://www.jetbrains.com/pycharm/download>`_
       4. **Slide** `ความรู้เบื้องต้นเกี่ยวกับการพัฒนาเว็บ <../../_static/courses/webdev/slides/wk01.html>`_ 
       5. **Code** `Github KhootClone Week01 <https://github.com/wichit2s/KhootClone/tree/week01>`_ 
   * - 2 
     - โครงสร้างของโครงงานและการรับส่งข้อมูล (HttpRequest,HttpResponse)

        **ผลลัพธ์การเรียนรู้**

       1. เข้าใจรูปแบบการส่งและรับข้อความระหว่างเครื่องผู้ใช้และเครื่องแม่ข่ายได้(client-server)
       2. อธิบายองค์ประกอบของข้อมูลคำร้อง (request) ได้
       3. อธิบายองค์ประกอบของข้อมูลส่งกลับ (response) ได้
       4. สร้างโครงงานและเขียนคำสั่งรับส่งข้อมูลได้

       .. collapse:: แบบฝึกหัดภาคทฤษฏี

         1. จงอธิบายรูปแบบการสื่อสารระหว่างเครื่องผู้ใช้ (client) และเครื่องแม่ข่าย (server) โดยระบุลักษณะการทำงานและตัวอย่างที่พบในชีวิตประจำวัน 
         2. จงอธิบายองค์ประกอบหลักของข้อมูลคำร้อง (HTTP Request) อย่างน้อย 3 รายการ พร้อมระบุหน้าที่ของแต่ละรายการ
         3. จงอธิบายองค์ประกอบหลักของข้อมูลส่งกลับ (HTTP Response) อย่างน้อย 3 รายการ พร้อมระบุหน้าที่ของแต่ละรายการ

       .. collapse:: แบบฝึกหัดภาคปฏิบัติ

          ส่งวีดีโอที่มีเสียงอธิบายประกอบเพื่อแสดงการปฏิบัติตามคำสั่งต่อไปนี้

         1. สร้างโครงงาน Django ชื่อ mysite 
         2. สร้าง url ที่สามารถเข้าถึงได้จาก /info ที่ส่งข้อมูลกลับเป็นข้อมูล python django ที่ระบุเวอร์ชัน
         3. สร้าง url ที่สามารถเข้าถึงได้จาก /hello ที่สามารถรับค่า name จากผู้ใช้ผ่านแบบฟอร์ม (POST) โดยให้เซิร์ฟเวอร์ตอบกลับด้วยข้อความ “Hello, [ชื่อผู้ใช้]” 
         4. สร้างแอปพลิเคชันชื่อ quiz ที่มี url ที่สามารถเข้าถึงได้แบบ GET ที่ /quiz/question ที่ส่งข้อมูลกลับเป็น JSON ในรูปแบบ {"id": 1, "text": "ประเทศไทยมีกี่จังหวัด", "choices": [50, 68, 72, 77]}
         5. เพิ่ม url ที่สามารถเข้าถึงได้แบบ POST ที่ /quiz/question/create ที่สามารถรับและส่งข้อมูลกลับเป็น JSON ในรูปแบบ {"id": 9, "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล", "choices": ["C", C++", "C#", "Python", "R", "Julia"]}
     - 1. `Chapter 2 Request and response objects <https://docs.djangoproject.com/en/5.0/ref/request-response/>`_
       2. `HTTP Messages <https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages>`_
       3. `Tutorial <https://docs.djangoproject.com/en/5.0/intro/tutorial01/>`_
       4. `PDF Response <https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/>`_
       5. :download:`Image Response <codes/chapter02/dynamic_image.py>` :icon:`fa-solid fa-download`
       6. **Slide** `โครงสร้างและการรับส่งข้อมูล <../../_static/courses/webdev/slides/wk02.html>`_ 
       7. **Code** `Github KhootClone Week02 <https://github.com/wichit2s/KhootClone/tree/week02>`_ 
   * - 3 - 4 
     - การจัดการข้อมูล (model)

        **ผลลัพธ์การเรียนรู้**

       1. อธิบายรูปแบบการกำหนดรูปแบบการจัดเก็บข้อมูลของ django ได้
       2. ประยุกต์ใช้ฟิลด์ (Field) ใน model ได้
       3. ประยุกต์ใช้คำสั่งค้นหา (query) ได้ตรงตามเงื่อนไขที่กำหนดให้  

       .. collapse:: แบบฝึกหัดภาคทฤษฏี

         1. อธิบายหลักการทำงานของ Django ORM ในการกำหนดรูปแบบการจัดเก็บข้อมูลผ่าน models.Modelel
         2. จงอธิบายความแตกต่างของ Field ต่อไปนี้: CharField, TextField, IntegerField, DateTimeField, ForeignKey

       .. collapse:: แบบฝึกหัดภาคปฏิบัติ

          ส่งวีดีโอที่มีเสียงอธิบายประกอบเพื่อแสดงการปฏิบัติตามคำสั่งต่อไปนี้

         1. สร้างโมเดลสำหรับรระบบ  quiz ที่มี Question(id, text, published_date)  และ Choice(id, question, text, correct)
         2. หลังจากสร้างและ migrate แล้ว ให้เขียนคำสั่ง query ตามโจทย์ต่อไปนี้ใน Django shell
          * ค้นหาคำถามทั้งหมด
          * ค้าหาคำถามที่มีคำว่า  AI ในคำถาม
          * ค้นหาคำถามที่เปิดหลังวันที่  1 กรกฏาคม 2565
          * ค้นหาคำถามมที่มี id เป็น 1
          * ค้นหาตัวเลือกทั้งหมดของคำถามมที่มี id เป็น 1

     - * Chapter 3 Models and databases

         * 3.1 `การติดต่อฐานข้อมูล <https://docs.djangoproject.com/en/5.0/ref/databases/>`_
         * 3.2 `การเขียน model class <https://docs.djangoproject.com/en/5.0/topics/db/models/>`_
         * 3.3 `การกำหนดข้อมูลตัวอย่าง (fixtures) <https://docs.djangoproject.com/en/5.0/howto/initial-data/>`_
         * 3.4 `การส่งคำสัง SQL โดยตรง  <https://docs.djangoproject.com/en/5.0/topics/db/sql/>`_
         * 3.5 `คำสั่งค้นหาข้อมูล <https://docs.djangoproject.com/en/5.0/topics/db/queries/>`_
         * 3.6 `การรวมผลลัพธ์ (Aggregation) <https://docs.djangoproject.com/en/5.0/topics/db/aggregation/>`_
         * 3.7 `คำสั่งค้นหา (Search) <https://docs.djangoproject.com/en/5.0/topics/db/search/>`_
       * `Tutorial <https://docs.djangoproject.com/en/5.0/intro/tutorial02/>`_
       * `ประเภทของฟิลด์ใน model <https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types>`_
       * **Slide** `3 - การจัดการข้อมูล <../../_static/courses/webdev/slides/wk03.html>`_ 
       * **Slide** `4 - การจัดการข้อมูลขั้นสูง <../../_static/courses/webdev/slides/wk04.html>`_ 
       * **Code** `Github Repo <https://github.com/wichit2s/KhootClone/tree/week03>`_
   * - 5 
     - การกำหนดการเข้าถึงและการแสดงผล (views,template)

        **ผลลัพธ์การเรียนรู้**

       1. อธิบายรูปแบบการกำหนดการเข้าถึงและการแสดงผลได้
       2. เขียนข้อกำหนดการเข้าถึงตามข้อกำหนดที่ระบุให้ได้
       3. ประยุกต์ใช้ความรู้เพื่อแสดงผลตามข้อกำหนดที่ระบุให้ได้

       .. collapse:: แบบฝึกหัดภาคทฤษฏี

         1. อธิบายหน้าที่ของ View ใน Django และอธิบายความแตกต่างระหว่าง Function-based View (FBV) และ Class-based View (CBV) 
         2. อธิบายหน้าที่ของ Template ใน Django และยกตัวอย่างการใช้ template tag เช่น {{ }} และ {% %}

       .. collapse:: แบบฝึกหัดภาคปฏิบัติ

          ส่งวีดีโอที่มีเสียงอธิบายประกอบเพื่อแสดงการปฏิบัติตามคำสั่งต่อไปนี้

         1. เพิ่ม function-based view เพื่อแสดงรายการคำถาม (Question) ทั้งหมด โดยสามารถเข้าถึงได้จาก quiz/func/list จากนั้นให้สร้าง question_list.html เพื่อแสดงชื่อบทความทั้งหมดในลักษณะรายการ (list)
         2. เพิ่ม function-based view และ template สำหรับแสดงรายละเอียดของคำถามพร้อมตัวเลือก เมื่อคลิกคำถามจากหน้า question_list.html โดยสามารถเข้าถึงได้จาก quiz/func/pk/
         3. เพิ่ม function-based view เพื่อแสดงรายการคำถามทั้งหมด โดยสามารถเข้าถึงได้จาก quiz/func/list?page=2 ที่สามารถเลือกหน้าแสดงรายการได้ หน้าละ 20 รายการ
         4. เพิ่ม class-based view เพื่อแสดงรายการคำถถาม (Question) ทั้งหมด โดยสามารถเข้าถึงได้จาก quiz/question/list  จากนั้นให้สร้าง question_list.html เพื่อแสดงชื่อบทความทั้งหมดในลักษณะรายการ (list)
         5. เพิ่ม class-based view และ template สำหรับแสดงรายละเอียดของคำถามพร้อมตัวเลือกก เมื่อคลิกคำถามจากหน้า question_list.html โดยสามารถเข้าถึงได้จาก quiz/question/pk/
         6. เพิ่ม class-based view และ template สำหรับแแสดงรายการคำถามทั้งหมด โดยสามารถเข้าถึงได้จาก quiz/question/list?page=2 ที่สามารถเลือกหน้าแสดงรายการได้ หน้าละ 20 รายการ

     - - `Chapter 4 Views and Templates <https://docs.djangoproject.com/en/5.0/intro/tutorial03/>`_
       - `Class-Based View <https://docs.djangoproject.com/en/5.2/topics/class-based-views/>`_
       - `Pagination <https://docs.djangoproject.com/en/5.2/topics/pagination/>`_
       - `HTML <https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML>`_
       - `คู่มือการเขียน template <https://docs.djangoproject.com/en/5.0/ref/templates/>`_
       * **Slide** `5 - view and templates <../../_static/courses/webdev/slides/wk05.html>`_ 
       - **Code** `Github Repo <https://github.com/wichit2s/KhootClone/tree/week05>`_
   * - 6
     - ฟอร์มและการแก้ไขข้อมูล (forms)

        **ผลลัพธ์การเรียนรู้**

       1. อธิบายรูปแบบการรับข้อมูลจากผู้ใช้และแก้ไขข้อมูลในฐานข้อมูลได้
       2. ประยุกต์ใช้ความรู้เพื่อสร้างฟอร์มในการรับข้อมูลจากผู้ใช้และแก้ไขข้อมูลในฐานข้อมูลโดยไม่ได้คลาสได้
       3. ประยุกต์ใช้ความรู้เพื่อสร้างฟอร์มในการรับข้อมูลจากผู้ใช้และแก้ไขข้อมูลในฐานข้อมูลโดยใช้คลาสได้

       .. collapse:: แบบฝึกหัดภาคทฤษฏี

         1. อธิบายกระบวนการรับข้อมูลจากผู้ใช้ใน Django และการบันทึก/แก้ไขข้อมูลในฐานข้อมูลโดยใช้ฟอร์ม
         2. อธิบายความแตกต่างระหว่างการสร้างฟอร์มโดยใช้ HTML ธรรมดา (manual form handling) กับการใช้ forms.Form หรือ forms.ModelForm ใน Django

       .. collapse:: แบบฝึกหัดภาคปฏิบัติ

          ส่งวีดีโอที่มีเสียงอธิบายประกอบเพื่อแสดงการปฏิบัติตามคำสั่งต่อไปนี้

         1. ให้เขียน view และ template สำหรับสร้างฟอร์ม HTML เพื่อรับข้อมูลคำถาม
         2. (Create) สร้างฟอร์มโดยใช้ forms.ModelForm
         3. (Update) แก้ไขข้อมูลโดยใช้ฟอร์ม 
         4. (CreateView) class-based view สำหรับสร้างงคำถาม
         6. (UpdateView) class-based view สำหรับแก้ไขคำถาม
     - - `Chapter 5 Forms <https://docs.djangoproject.com/en/5.0/intro/tutorial04/>`_
       - `การสร้างฟอร์มโดยใช้คลาส <https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/>`_
       * **Slide** `6 - Forms and CRUD <../../_static/courses/webdev/slides/wk06.html>`_ 
       - **Code** `Github Repo <https://github.com/wichit2s/KhootClone/tree/week06>`_
   * - 7 
     - การกำหนดสิทธิ์เข้าใช้งาน (login,logout)

        **ผลลัพธ์การเรียนรู้**

       1. อธิบายรูปแบบการจัดเก็บข้อมูลผู้ใช้โดย django ได้
       2. ประยุกต์ใช้ความรู้เพื่อสร้างฟอร์มในการรับลงทะเบียนผู้ใช้ใหม่ได้
       3. ประยุกต์ใช้ความรู้เพื่อสร้างฟอร์มในการตรวจสอบผู้ใช้เข้าใช้งานได้

       .. collapse:: แบบฝึกหัดภาคทฤษฏี

         1. อธิบายกระบวนการรับข้อมูลจากผู้ใช้ใน Django และการบันทึก/แก้ไขข้อมูลในฐานข้อมูลโดยใช้ฟอร์ม
         2. อธิบายความแตกต่างระหว่างการสร้างฟอร์มโดยใช้ HTML ธรรมดา กับการใช้ forms.Form หรือ forms.ModelForm ใน Django

       .. collapse:: แบบฝึกหัดภาคปฏิบัติ

          ส่งวีดีโอที่มีเสียงอธิบายประกอบเพื่อแสดงการปฏิบัติตามคำสั่งต่อไปนี้

         1. ให้เขียน view และ template สำหรับสร้างฟอร์ม HTML เสำหรับลงทะเบียนผู้ใช้งาน
         2. ให้เขียน view และ template สำหรับสร้างฟอร์ม HTML สำหรับการล็อกอินน์สมาชิก
         3. เขียน RegisterView และ template สำหรับลงทะเบียนผู้ใช้
         3. เขียน LoginView และ template สำหรับลงล็อกอินสมาชิก
     - - `Chapter 6 Authentication <https://docs.djangoproject.com/en/5.0/topics/auth/default/>`_
       * **Slide** `7 - Django Authentication <../../_static/courses/webdev/slides/wk07.html>`_ 
       - **Code** `Github Repo <https://github.com/wichit2s/KhootClone/tree/week06>`_
   * - 8 
     - ไฟล์และรูปแบบคำสั่งแสดงผล (static files and template engine)
        **ผลลัพธ์การเรียนรู้**
       1. อธิบายรูปแบบการจัดเก็บไฟล์ของเว็บไซต์และการอ้างอิงใน django ได้
       2. ประยุกต์ใช้ความรู้เพื่อแทรกไฟล์(ภาพ,วีดีโอ,เสียง)ใน template ของ response สำหรับแสดงผลได้
       3. ประยุกต์ใช้ความรู้เพื่อกำหนดการแสดงผลโดยใช้ CSS เบื้องต้นได้
     - - `Chapter 7 Static files and Templates <https://docs.djangoproject.com/en/5.0/intro/tutorial06/>`_
       - `CSS เบื้องต้น <https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Getting_started>`_
   * - 9 
     - CSS Library
        **ผลลัพธ์การเรียนรู้**
       1. อธิบายรูปแบบการจัดเก็บไฟล์ของเว็บไซต์และการอ้างอิงใน django ได้
       2. ประยุกต์ใช้ความรู้เพื่อแทรกไฟล์(ภาพ,วีดีโอ,เสียง)ใน template ของ response สำหรับแสดงผลได้
       3. ประยุกต์ใช้ความรู้เพื่อกำหนดการแสดงผลโดยใช้ CSS เบื้องต้นได้
     - - `Chapter 8 Bulma CSS <https://bulma.io/documentation>`_
       - `การกำหนดการแสดงภาพโดยใช้ tailwindcss <https://www.geeksforgeeks.org/tailwind-css>`_ 
   * - 10
     - JavaScript fundamentals
        **ผลลัพธ์การเรียนรู้**
       1. อธิบายรูปแบบการเขียนคำสั่งภาษา JavaScript ได้
       2. ประยุกต์ใช้ความรู้ชุดคำสั่ง client-side web API เบื้องต้นได้
     - - `Chapter 9.1 JavaScript <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Language_overview>`_
       - `Chapter 9.2 Client-Side Web API <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs>`_
   * - 11 
     - HTMX
        **ผลลัพธ์การเรียนรู้**
       1. ประยุกต์ใช้ความรู้ชุดคำสั่ง htmx เพื่อร้องขอข้อมูลจาก backend ได้
     - - `Chapter 10 HTMX <https://htmx.org/docs/>`_
       - `เอกสารเสริมเรื่อง hyperscript <https://hyperscript.org/docs/>`_
   * - 12 
     - Alpinejs
        **ผลลัพธ์การเรียนรู้**
       1. ประยุกต์ใช้ความรู้ชุดคำสั่ง alpinejs เพื่อจัดการการแสดงผลแบบพลวัตได้
     - - `Chapter 11 Alpinejs <https://alpinejs.dev>`_
   * - 13 
     - การทดสอบ (testing)
     - - `Chapter 12 Testing <https://docs.djangoproject.com/en/5.0/intro/tutorial05/>`_
       - `คู่มือการเขียนทดสอบ django <https://docs.djangoproject.com/en/5.0/topics/testing/overview/>`_
   * - 14 
     - เนื้อหาต่อยอด
     - - `รูปแบบการงานร่วมกับ javascript framework ที่เป็นที่นิยม <https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/>`_
       - `การสร้างโครงงานระดับสูง <https://cookiecutter-django.readthedocs.io/en/latest/>`_
   * - 15 
     - นำเสนอโครงงาน
     - นักศึกษานำเสนอผลงาน


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   project


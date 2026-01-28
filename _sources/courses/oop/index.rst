.. image:: ./oop_banner.jpg

การเขียนโปรแกรมเชิงวัตถุ
====================================

.. warning::

  เอกสารชุดนี้อยู่ในระหว่างการปรับปรุง


.. list-table:: ตารางหลักสูตรการเขียนโปรแกรมเชิงวัตถุ
   :header-rows: 1
   :widths: 5 35 35 25

   * - **สัปดาห์**
     - **เนื้อหาหลักสูตร**
     - **วัตถุประสงค์การเรียนรู้**
     - **แหล่งที่มาเอกสาร**
   * - **1**
     - ภาพรวมของรายวิชา (Course Overview)
        1. ประวัติของการเขียนโปรแกรมเชิงวัตถุ 
        2. บทนำสู่คลาสและออบเจกต์
     - * เข้าใจภาพรวมของ OOP และรู้จักคลาสและออบเจกต์พื้นฐาน 
     - 1. `The Python Language Reference <https://docs.python.org/3/reference/index.html>`_
       2. `การติดตั้ง <https://www.slideshare.net/slideshow/python-dev-setup-thaipdf/253351612>`_ 

          * `scoop <https://scoop.sh/>`_
           - git
           - anaconda3
          * `สมัครใช้ pycharm professional <https://www.jetbrains.com/shop/eform/students>`_
          * `download pycharm professional <https://www.jetbrains.com/pycharm/download>`_
   * - **2**
     - แอททริบิวต์และเมธอด (Attributes and Methods)
        1. ความแตกต่างระหว่างการเขียนโปรแกรมเชิงขั้นตอนและเชิงวัตถุ
     - * อธิบายแอททริบิวต์และเมธอดในคลาสได้ 
     - * `Python Classes <https://docs.python.org/3/tutorial/classes.html>`_
   * - **3**
     - การห่อหุ้มข้อมูล (Encapsulation)
        1. การซ่อนข้อมูล 
        2. การกำหนดสิทธิ์การเข้าถึง (สาธารณะ ส่วนตัว ป้องกัน)
     - * เข้าใจการห่อหุ้มข้อมูลและการซ่อนข้อมูลในคลาส 
     - * `Encapsulation <https://realpython.com/python3-object-oriented-programming/>`_
       * `Encapsulation Note <./concepts/encapsulation.html>`_
   * - **4** 
     - การสืบทอด (Inheritance)
        1. ประเภทของการสืบทอดแบบ Single
        2. ประเภทของการสืบทอดแบบ Multiple
        3. ประเภทของการสืบทอดแบบ Hierarchical
     -  * ประยุกตใช้การสืบทอดแบบ Single
        * ประยุกต์ใช้การสืบทอดแบบ Multiple, Mixins
        * ประยุกต์ใช้การสืบทอดแบบ Hierarchical 
     - * `Inheritance <https://docs.python.org/3/tutorial/classes.html#inheritance>`_
       * `Inheritance Note <./concepts/inheritance.html>`_
   * - **5**
     - โพลีมอร์ฟิซึม (Polymorphism)
        1. การทำงานร่วมกันของเมธอดแบบ Overloading
        2. การทำงานร่วมกันของเมธอดแบบ Overriding
     - * เข้าใจแนวคิดของโพลีมอร์ฟิซึม
       * เข้าใจวิธีการ Overloading
       * เข้าใจวิธีการ Overriding 
     - * `Polymorphism <./concepts/polymorphism.html>`_
   * - **6**
     - นามธรรมและอินเทอร์เฟซ (Abstraction and Interface)
        1. คลาสนามธรรม
        2. อินเทอร์เฟซ
     - * เข้าใจแนวคิดของนามธรรมและการใช้อินเทอร์เฟซ 
     - * `Abstract Base Class <https://docs.python.org/3/library/abc.html>`_
   * - **7**
     - คอมโพสซิชัน (Composition)
        1. ความสัมพันธ์แบบ Association
        2. ความสัมพันธ์แบบ Aggregation
        3. ความสัมพันธ์แบบ Composition
     - 1. ประยุกต์ใช้หลักการ Composition และ Inheritance
       2. อธิบายข้อแตกต่างระหว่าง Composition และ Inheritance 
     - * `Composition vs Inheritance <https://realpython.com/inheritance-composition-python>`_
   * - **8**
     - บทนำสู่ UML (Unified Modeling Language)
        1. Class Diagram
        2. Sequence Diagram
     - * ใช้ UML ในการวางแผนโครงสร้างโปรแกรม 
     - `UML Introduction <https://www.geeksforgeeks.org/unified-modeling-language-uml-introduction/>`_
   * - **9**

       :icon:`fa fa-link` `สไลด์ <../../_static/courses/oop/slides/wk09.html>`_
     - ทบทวนเนื้อหา OOP และ UML เพื่อการพัฒนาโปรเจกต์
     - * อธิบายความรู้เพื่อเตรียมพร้อมสำหรับการประยุกต์ใช้ในโปรเจกต์ 
     - * `OOP Concepts <./concepts/index.html>`_
       * `UML Introduction <https://www.geeksforgeeks.org/unified-modeling-language-uml-introduction/>`_
       * `Github Guide <https://www.geeksforgeeks.org/ultimate-guide-git-github/>`_
   * - **10**

       :icon:`fa fa-link` `สไลด์ <../../_static/courses/oop/slides/wk10.html>`_
     - บทนำสู่ Design Patterns ในโปรแกรมเชิงวัตถุ
        * Design Patterns
        * SOLID Principles
     - * เข้าใจแนวคิดการออกแบบ Design Patterns 
       * เข้าใจหลักการ SOLID 
     - * `Design Patterns <https://www.geeksforgeeks.org/software-design-patterns/>`_
       * `SOLID Principles <https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/>`_
   * - **11,12,13**
     - พัฒนาโปรเจกต์และประยุกต์ใช้แนวคิดเชิงวัตถุ
        Object-Oriented Application Frameworks
       1. `pygame note <./oop-in-pygame/index.html>`_  /  `pygame <https://pygame.org/docs>`_ 
       2. `pyside6 note <./oop-in-pyside/index.html>`_ /  `pyside6 <https://doc.qt.io/qtforpython-6/gettingstarted.html>`_
       3. `machine learning note <./oop-in-ml/index.html>`_  / `scikitlearn iris svc plot <https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html>`_
       4. `fastapi <https://fastapi.tiangolo.com/tutorial/>`_
       5. `AI (transformer models) <https://huggingface.co/docs/transformers/index>`_
     - 1. เข้าใจหลักการพัฒนาชุดคำสั่งเสริมที่ใช้แนวคิดเชิงวัตถุ
       2. อธิบายหลักการใช้งานชุดคำสั่งเสริมที่ใช้แนวคิดเชิงวัตถุเพื่อนำมาแก้ปัญหาโจทย์ที่กำหนดให้ได้ 
        :icon:`fa-solid fa-person-running` `เกณฑ์การประเมิน <./project_criteria.html>`_
     - * `pygame note <./oop-in-pygame/index.html>`_  /  `pygame <https://pygame.org/docs>`_ 
       * `pyside6 note <./oop-in-pyside/index.html>`_ /  `pyside6 <https://doc.qt.io/qtforpython-6/gettingstarted.html>`_
       * `machine learning note <./oop-in-ml/index.html>`_  / `scikitlearn iris svc plot <https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html>`_
       * `fastapi <https://fastapi.tiangolo.com/tutorial/>`_
       * `AI (transformer models) <https://huggingface.co/docs/transformers/index>`_
   * - **14**
     - เตรียมการนำเสนอโปรเจกต์ และสรุปความรู้ OOP ที่ได้เรียนรู้
     - เตรียมการนำเสนอและสรุปผลการเรียนรู้ในโปรเจกต์
     - `Project Preparation <https://example.com/14>`_
   * - **15**
     - การนำเสนอโปรเจกต์และตอบข้อซักถาม สรุปผลการเรียนรู้ทั้งหมด
     - 1. สามารถนำเสนอให้เข้าใจโครงงานได้ง่าย สื่อสารโดยใช้เทคโนโลยีที่เหมาะสม ตอบคำถามด้วยความเข้าใจและมีหลักการ
        :icon:`fa-solid fa-person-running` `เกณฑ์การประเมิน <./project_criteria.html>`_
     - Final Presentation


     
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   oop-in-pygame/slide



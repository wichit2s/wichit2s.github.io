****************************************
คอมพิวเตอร์และโปรแกรม
****************************************

Computers and Programs

|Download|

จุดประสงค์
========================================

1. เข้าใจการทำงานของโปรแกรมที่เขียนด้วยภาษา Python

-  สร้าง แก้ไข และ run โปรแกรมบน spyder ได้
-  เขียนคำสั่งบน ipython ได้
-  สร้าง jupyter notebook ได้
-  เขียนคำสั่งและ run บน notebook ได้

2. เขียนโปรแกรมเพื่อแสดงข้อความ "สวัสดีชาวโลก" ได้
3. เขียนโปรแกรมเพื่อรับชื่อและแสดงข้อความ "สวัสดีคุณชื่อ" ได้

.. |Download| image:: icons/colab-logo.png
   :target: https://drive.google.com/file/d/1A_SnlOVGOeIlcn9FLu6Pn7fKNJKkCNb0

Computer Hardware
========================================

.. figure:: images/hardware.png
   :alt: hardware

   hardware

   
Computer Software (Programs)
========================================

A. [แปลง] Compiled Programming Languages
----------------------------------------

.. figure:: images/compiled-program.png
   :alt: compile-program

   compile-program

ตัวอย่างภาษาโปรแกรมที่เป็นแบบ Compiled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `C <https://en.cppreference.com/w/c>`__
-  `C++ <https://en.cppreference.com/w/>`__
-  `Go <https://go.dev/>`__
-  `Java <https://www.java.com/en/>`__
-  `Swift <https://www.swift.org/>`__
-  `Rust <https://www.rust-lang.org/>`__

B. [แปล] Interpreted Program
----------------------------------------

.. figure:: images/interpreted-program.png
   :alt: interpreted-program

   interpreted-program

ตัวอย่างภาษาโปรแกรมที่เป็น interpreted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `Python <https://www.python.org/>`__
-  `TypeScript <https://www.typescriptlang.org/>`__
-  `JavaScript <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide>`__
-  `PHP <https://www.php.net/manual/en/langref.php>`__
-  `R <https://cran.r-project.org/doc/manuals/r-release/R-intro.html>`__
-  `Lisp <https://quickdocs.org/>`__


ไพธอน (Python)
========================================

-  ภาษาโปรแกรมเชิงวัตถุสำหรับใช้งานหลายด้าน
-  รองรับหลายระบบปฏิบัติการ
-  เขียนง่าย อ่านง่าย
-  มีชุดคำสั่งเสริมมากมาย สำหรับหลากหลายด้าน

ทำไมไพธอนมีคนใช้เยอะ?
============================================================

เป็นภาษาโปรแกรมที่นิยมใช้ในการพัฒนาซอฟตแวร์
------------------------------------------------------------

-  `Top 10 Most Popular Programming Languages to Learn in
   2020 <https://www.northeastern.edu/graduate/blog/most-popular-programming-languages/>`__
   ``Northe Eastern University``
-  `10 Most Popular Programming Languages in October 2020: Learn To
   Code <https://www.guru99.com/best-programming-language.html>`__
   ``guru99``
-  `TIOBE Index <https://www.tiobe.com/tiobe-index/>`__

เป็นภาษาโปรแกรมที่นิยมใช้ในงานด้านวิทยาการข้อมูล
------------------------------------------------------------

-  `Top programming languages use to compete in kaggle
   competition <https://www.kaggle.com/tvirot/top-languages-used>`__
   ``kaggle``
-  `Top 10 Data Science Programming Languages for
   2020 <https://www.analyticsinsight.net/top-10-data-science-programming-languages-for-2020/>`__
   ``analyticsinsight``
-  `Top Programming Languages for Data Science in
   2020 <https://www.geeksforgeeks.org/top-programming-languages-for-data-science-in-2020/>`__
   ``geeksforgeeks``
-  `Top Data Science Programming
   Languages <https://jelvix.com/blog/top-data-science-programming-languages>`__
   ``jelvix``
-  `Top 7 Best Programming Languages for Data
   Science <https://techbiason.com/programming-languages-for-data-science/>`__
   ``techbiason``

เป็นภาษาโปรแกรมที่ได้รับความนิยมในการพัฒนาระบบ IoT
------------------------------------------------------------

   -  `Top Programming Languages for IoT
      Projects <https://orangesoft.co/blog/top-programming-languages-for-iot-projects>`__
      ``orangesoft``
   -  `7 Best Languages to Learn IoT Development in
      2020 <https://www.geeksforgeeks.org/7-best-languages-to-learn-iot-development-in-2020/>`__
      ``geeksforgeeks``
   -  `Top 8 Programming Languages for IoT (with
      Examples) <https://howtocreateapps.com/programming-languages-iot/>`__
      ``howtocreateapps``
   -  `What programming languages rule the Internet of
      Things? <https://www.networkworld.com/article/3336867/what-programming-languages-rule-the-internet-of-things.html>`__
      ``networkworld``
   -  `Best Programming Languages for IoT in
      2020 <https://www.electronicsmedia.info/2020/11/19/best-programming-languages-for-iot-in-2020/>`__
      ``electronicsmedia``


เริ่มการเขียนคำสั่ง
========================================

-  คำสั่งสำหรับนำเข้าชุดคำสั่ง sys เพื่อเรียกใช้ฟังก์ชัน version
   เพื่อดูรายละเอียดของ Python

   .. code:: python

       import sys
       sys.version

กรอกคำสั่งตรงช่องด้านล่าง แล้ว click รัน หรือกดปุ่ม Shift พร้อม Enter บน
keyboard


-  คำสั่งแสดงข้อความบนหน้าจอ

   .. code:: python

       print('ข้อความ')

-  ตัวอย่างคำสั่งแสดงข้อความอื่นๆ

   .. code:: python

       print('Hello world')
       print("Hello world")
       print('สวัสดีชาวโลก')
       print("สวัสดีชาวโลก")


-  **Exercise 01.1** จงเขียนคำสั่งเพื่อแสดงชื่อของตัวเอง เป็นภาษาไทย

-  **Exercise 01.2** จงเขียนคำสั่งเพื่อแสดงชื่อเล่น

-  **Exercise 01.3** จงเขียนคำสั่งเพื่อแสดงชื่อของตัวเอง เป็นภาษาอังกฤษ

-  **Exercise 01.4** ลองเขียนคำสั่งเพื่อแสดง email ของตัวเอง


การแสดงผลการคำนวณเบื้องต้น
========================================

-  คำสั่งแสดงผลบวก

   .. code:: python

       print(2+3)

-  คำสั่งแสดงผลลบ

   .. code:: python

       print(2561-543)

-  คำสั่งแสดงผลคูณ

   .. code:: python

       print(9*1024)

-  คำสั่งแสดงผลหาร

   .. code:: python

       print(1024/7)

-  คำสั่งแสดงผลยกกำลัง

   .. code:: python

       print(10**2)
       print(2**10)

-  คำสั่งแสดงผลค่ารากที่สองตัวเลข

   .. code:: python

       print(100**0.5)

-  คำสั่งแสดงผลของสมการที่ซับซ้อนขึ้น

   .. code:: python

       print( (2*3 + 3*3 + 1*3 + 2*3 + 2*3)/(3+3+3+3) )


-  **Exercise 01.5** จงเขียนคำสั่งเพื่อแสดงผลลัพธ์ของสมการต่อไปนี้

   -  :math:`2^3 + 9 \times 7`

   -  :math:`\frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5}`

   -  :math:`\sqrt{3^2 - 4\times 1 \times 2}`

   -  :math:`\frac{\sqrt{4\times 3 \times 7}}{2 \times 3}`


การแสดงข้อความร่วมกับตัวเลข
========================================

.. code:: python

    print('ผลลัพธ์ ', 2**20)
    print('สวัสดีคุณ', 'พอล')
    print('สวัสดีคุณ'+'พอล')
    print('สวัสดีคุณ'+str(2**20))

Note: ``str()`` แปลงค่าให้เป็นข้อความ


การรวมหลายคำสั่งเป็นฟังก์ชัน
========================================

1. (ให้นิยาม) กำหนดชื่อและการทำงานของฟังก์ชัน

.. code:: python

    def hello():
        print('Hello world')
        print("Hello world")
        print('สวัสดีชาวโลก')
        print("สวัสดีชาวโลก")

2. (เรียกใช้ฟังก์ชัน) คำสั่งเรียกใช้

.. code:: python

    hello()

3. ตัวอย่างฟังก์ชัน

.. code:: python

    def print9():
        print(' 9x1 =  9')
        print(' 9x2 = 18')
        print(' 9x3 = 27')
        print(' 9x4 = 36')
        print(' 9x5 = '+str(9*5))
        print(' 9x6 = ', 9*6)

-  **Exercise 01.6** จงเขียนฟังก์ชันแสดงสูตรคูณแม่ต่างๆ พร้อมเรียกใช้

   -  สูตรคูณแม่ 4
   -  สูตรคูณแม่ 7
   -  สูตรคูณแม่ 12


การเรียกใช้ฟังก์ชันที่พร้อมใช้งาน
========================================

    ฟังก์ชันที่เรียกใช้ได้เลย `รายชื่อ built-in functions
    ทั้งหมด <https://docs.python.org/3/library/functions.html>`__

1. กลุ่มฟังก์ชันแปลงชนิดข้อมูล
----------------------------------------

   .. code:: python

       bin(8)         # แปลงตัวเลขเป็นเลขฐานสอง
       bool(1)        # แปลงเป็นค่าเท็จจริง True, False
       chr(3585)      # แปลงตัวเลขเป็นตัวอักขระ
       float('3.55')  # แปลงเป็นเลขทศนิยม
       hex(20)        # แปลงเป็นเลขฐาน 16
       id(1)          # แปลงเป็นหมายเลขรหัส
       int(3.2)       # แปลงเป็นจำนวนเต็ม
       oct(9)         # แปลงเป็นเลขฐาน 8
       ord('ก')       # แปลงอักขระเป็นจำนวนเต็ม
       str(619009499) # แปลงเป็นข้อความ

2. กลุ่มฟังก์ชันให้ช่วยเหลือ
----------------------------------------

   .. code:: python

       dir()           # แสดงรายการฟังก์ชันที่สามารถเรียกใช้งานได้
       help()          # ขอความช่วยเหลือกับคำสั่งต่างๆ
       type('ข้อความ')   # แสดงชนิดของข้อมูล

3. กลุ่มฟังก์ชันสำหรับการประมวลผลอื่นๆ
----------------------------------------

A. ฟังก์ชันนำเข้าข้อมูล - input -

.. code:: python

    input()                 # ฟังก์ชันนำเข้าข้อความ (ให้ผู้ใช้กรอกจากคีย์บอร์ด)
    input('กรุณากรอกข้อมูล ')  # ฟังก์ชันนำเข้าข้อความพร้อมข้อความบอกผู้ใช้ 

B. ฟังก์ชันช่วยในการประมวลผล - process -

.. code:: python

    format(  1234, '<15d')
    format('1234', '>15s')
    format(  1234, '^15d')
    min( [5,9,7,6,5,4] )
    max( [5,9,7,3,7,1] )
    len( [1,9,3,4,4] )
    open('test.txt', 'r')
    pow(2, 10)
    range(10)
    round(3.6)
    round(3.4)
    sorted( [1,9,3,4,4] )
    sum( [1,9,3,4,4] )

C. ฟังก์ชันแสดงข้อความ - output -

.. code:: python

    print('ข้อความที่ต้องการให้ผู้ใช้เห็น')


การเก็บข้อความที่ผู้ใช้กรอกเพื่อใช้งาน
========================================

-  การนำเข้าข้อความที่ผู้ใช้กรอกเก็บไว้สำหรับอ้างอิงต่อไปโดยใช้ชื่อ x

   .. code:: python

       x = input()

-  การแสดงค่าที่ x อ้างอิงถึง

   .. code:: python

       print(x)

-  หลักเกณฑ์ในการตั้งชื่อตัวอ้างอิง (identifier) บางคนเรียก ตัวแปร -
   variable

1. เป็นลำดับของตัวอักษรติดกันแต่ละอันสามารถใช้ a-z, A-Z, 0-9, \_
   โดยไม่จำกัดความยาว
2. ตัวแรกต้องไม่เป็นตัวเลข
3. ต้องไม่เป็น keywords (คำสงวน)
4. ต้องไม่เป็นค่า literals - ชุดของอักขระที่ Python
   สามารถแปลงเป็นค่าได้ทันที เช่น 'Paul' 342.0 เป็นต้น

-  คำสงวน (keywords) ในภาษา Python มีอะไรบ้าง?

   .. code:: python

       False      class      finally    is         return
       None       continue   for        lambda     try
       True       def        from       nonlocal   while
       and        del        global     not        with
       as         elif       if         or         yield
       assert     else       import     pass
       break      except     in         raise

-  **Exercise 01.7** ฝึกตั้งชื่อตัวอ้างอิงหรือตัวแปร

   -  ตัวแปรสำหรับเก็บชื่อผู้ใช้
   -  ตัวแปรสำหรับเก็บอายุผู้ใช้
   -  ตัวแปรสำหรับเก็บค่า x
   -  ตัวแปรสำหรับเก็บค่า y
   -  ตัวแปรสำหรับเก็บค่า z
   -  ตัวแปรสำหรับเก็บค่าปีเกิด
   -  ตัวแปรสำหรับเก็บค่าเกรดเฉลี่ย
   -  ตัวแปรสำหรับเก็บค่าความสูงของระดับน้ำในแม่โขง
   -  ตัวแปรสำหรับเก็บค่าระยะทางจากวารินไปยังทุ่งศรีเมือง


การรับข้อความและแปลงเป็นค่าต่างๆ
========================================

-  การรับข้อความแล้วแปลงเป็นตัวเลข

   .. code:: python

       x = input()
       age = int(x)

-  การรับข้อความแล้วแปลงเป็นตัวเลขโดยใช้คำสั่งซ้อนคำสั่ง

   .. code:: python

       age = int(input())

-  การรับข้อความแล้วแปลงเป็นเลขทศนิยม

   .. code:: python

       x = input()
       gpa = float(x)

-  การรับข้อความแล้วแปลงเป็นเลขทศนิยมโดยใช้คำสั่งซ้อนคำสั่ง

   .. code:: python

       gpa = float(input())

-  **ตัวอย่าง** การเขียนโปรแกรมเพื่อรับชื่อผู้ใช้

   .. code:: python

       name = input('ชื่ออะไรครับ? ')
       print('สวัสดีครับคุณ'+name)

-  **ตัวอย่าง** การเขียนโปรแกรมเพื่อรับชื่อผู้ใช้

   .. code:: python

       name = input('What is your name? ')
       print('Hello, '+name)

-  **ตัวอย่าง** การเขียนโปรแกรมเพื่อรับอายุผู้ใช้

   .. code:: python

       x = input('อายุเท่าไหร่? ')
       age = int(x)
       print('คุณอายุ '+str(age)+' ปี')

-  **ตัวอย่าง** การเขียนโปรแกรมเพื่อรับค่า x กับ y แล้วบอกผลบวก

   .. code:: python

       x = int(input('x = '))
       y = int(input('y = '))
       print(' x + y = '+str( x+y ))


-  **Exercise 01.7** จงเขียนโปรแกรมเพื่อให้ทำงานตามโจทย์ต่อไปนี้

   -  จงเขียนโปรแกรมเพื่อรับค่า x กับ y แล้วบอกผลต่าง

   -  จงเขียนโปรแกรมเพื่อรับค่า x กับ y แล้วบอกผลคูณ

   -  จงเขียนโปรแกรมเพื่อรับค่า x กับ y แล้วบอกผลหาร

   -  จงเขียนโปรแกรมเพื่อรับค่า x กับ y แล้วบอกผลลัพธ์เมื่อเอาค่า x
      ยกกำลัง y :math:`x^y`

   -  จงเขียนโปรแกรมเพื่อรับค่าปี พ.ศ.เกิดของผู้ใช้ แล้วบอกอายุ

   -  จงเขียนโปรแกรมเพื่อรับค่าปี พ.ศ.เกิดของผู้ใช้
      แล้วบอกปีเกิดของผู้ใช้เป็น ค.ศ.

   -  จงเขียนโปรแกรมเพื่อรับค่าเกรดเฉลี่ยของเทอมต้น
      และเกรดเฉลี่ยของเทอมปลาย แล้วบอกเกรดเฉลี่ยรวมในปีนั้น


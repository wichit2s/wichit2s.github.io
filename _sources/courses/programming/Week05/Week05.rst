
การเขียนฟังก์ชัน
================

|Binder| |Download|

    Defining Functions

จุดประสงค์
----------

1. เข้าใจเหตผลของการแบ่งคำสั่งหลักออกเป็นหลายฟังก์ชันย่อย
2. สามารถเขียนฟังก์ชันด้วยภาษา Python ได้
3. เข้าใจการเรียกใช้ฟังก์ชันและการส่งผ่านข้อมูล
4. สามารถเขียนโปรแกรมที่ใช้ฟังก์ชันเพื่อลดความซ้ำซ้อนและเป็นระเบียบได้

ความรู้เบื้องต้น
----------------

สรุปประเภทของฟังก์ชันที่ใช้มาก่อนหน้านี้
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. ฟังก์ชันที่สามารถเรียกใช้ได้เลยโดยที่ไม่ต้องเขียนเอง เรียกว่า
   built-in functions เช่น ``input(), print()`` เป็นต้น
2. ฟังก์ชันจากชุดคำสั่งเสริมที่เป็นมาตรฐานของไพธอน เรียกว่า standard
   library เช่น ``math.cos`` เป็นต้น
3. ฟังก์ชันที่ผู้พัฒนาเขียนขึ้นมาเพื่อเรียกใช้งานเอง

ประโยชน์ของฟังก์ชัน
~~~~~~~~~~~~~~~~~~~

1. ช่วยลดการเขียนคำสั่งที่ซ้ำซ้อน
2. ช่วยทำให้คำสั่งกระชับทำความเข้าใจได้ง่ายขึ้น
3. ช่วยให้การปรับปรุงหรือแก้ไขข้อผิดพลาดนั้นทำที่ตำแหน่งเดียว

แนวคิดและที่มาของฟังก์ชัน
~~~~~~~~~~~~~~~~~~~~~~~~~

ฟังก์ชันเหมือนส่วนย่อยของโปรแกรมที่รวมชุดของคำสั่งที่มีความซับซ้อนในการทำงาน
เพื่อให้สามารถเรียกใช้งานใหม่ได้ทุกครั้งที่ต้องการโดยเรียกใช้ชื่ออ้างอิงเท่านั้น

-  การประกาศชุดคำสั่งเป็นฟังก์ชัน เรียกว่า function definition
-  การเรียกใช้ฟังก์ชัน เรียกว่า function call หรือ function invocation

การประกาศฟังก์ชัน
-----------------

**รูปแบบ**

.. code:: python

    def ชื่อฟังก์ชัน(ลำดับของตัวแปร):
        คำสั่ง
        คำสั่ง
        คำสั่ง
        ...

**ภาษาอังกฤษ**

.. code:: python

    def function_name( parameters_list ):
        statement
        statement
        statement
        ...

หรือ

.. code:: python

    def function_name( function_parameters ):
        function_body

.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gl/wichit2s%2Fprogrammingfundamentals/master?filepath=Week05%2FWeek05.ipynb
.. |Download| image:: ../icons/download.png
   :target: https://gitlab.com/wichit2s/programmingfundamentals/raw/master/Week05/Week05.ipynb?inline=false

ฟังก์ชันที่ไม่มี ``parameters``
-------------------------------

โปรแกรมแสดงเนื้อเพลง happy birthday 3 รอบ

.. code:: python

    print('Happy birthday to you')
    print('Happy birthday to you')
    print('Happy birthday dear Anna')
    print('Happy birthday to you.')

    print('Happy birthday to you')
    print('Happy birthday to you')
    print('Happy birthday dear Anna')
    print('Happy birthday to you.')

    print('Happy birthday to you')
    print('Happy birthday to you')
    print('Happy birthday dear Anna')
    print('Happy birthday to you.')

ความซ้ำซ้อนนี้สามารถนำมาเขียนเป็นฟังก์ชันได้เป็นการแสดงเนื้อเพลงเป็นฟังก์ชันได้ดังนี้

**การประกาศฟังก์ชัน (Function Definition)**

.. code:: python

    def happybdayAnna():
        print('Happy birthday to you')
        print('Happy birthday to you')
        print('Happy birthday dear Anna')
        print('Happy birthday to you.')

**การเรียกใช้ฟังก์ชัน (Function Call)**

.. code:: python

    happybdayAnna()
    happybdayAnna()
    happybdayAnna()


Exercises
---------

-  จงประกาศฟังก์ชัน happybdayPaul() เพื่อแสดงเนื้อเพลง happy birthday
   ให้กับ ``Paul``

-  จงแสดงคำสั่งเรียกใช้ฟังก์ชัน happybdayPaul() 4 ครั้ง

-  จงแสดงคำสั่งเรียกใช้ฟังก์ชัน happybdayPaul() 25 ครั้ง

-  จงประกาศฟังก์ชัน happybdayJohn() เพื่อแสดงเนื้อเพลง happy birthday
   ให้กับ ``John``

-  จงแสดงคำสั่งเรียกใช้ฟังก์ชัน happybdayJohn() 10 ครั้ง


ฟังก์ชันที่มี ``parameter``
---------------------------

ฟังก์ชัน happybday ที่สามารถเปลี่ยนชื่อเจ้าของวันเกิดได้

.. code:: python

    happybday('Anna')
    happybday('Elsa')
    happybday('Olaf')

การประกาศฟังก์ชัน happybday ที่สามารถระบุชื่อได้

.. code:: python

    def happybday(name):
        print('Happy birthday to you')
        print('Happy birthday to you')
        print(f'Happy birthday dear {name}')
        print('Happy birthday to you.')

**parameter** หมายถึงตัวแปรที่สร้างขึ้นเมื่อมีการเรียกฟังก์ชัน (function
call)

    จากตัวอย่างข้างต้น happybday เป็นฟังก์ชันที่มี parameter 1 ตัวคือ
    name

**argument** เป็นค่าที่ส่งให้ฟังก์ช้นเมื่อมีเรียกฟังก์ชัน (function
call) เช่น

.. code:: python

    happybday('Anna') 

    argument ของคำสั่ง ``happybday('Anna')`` คือ ``'Anna'``

.. code:: python

    name = 'Paul'
    happybday(name) 

    argument ของ ``happybday(name)`` คือ ``'Paul'``


Exercises
---------

-  จงเขียนฟังก์ชันชื่อ repeatbday เพื่อรับ parameter 1 ตัวชื่อ n
   โดยฟังก์ชัน repeatbday(n) จะต้องแสดงเนื้อเพลง happydbay('Paul') จำนวน
   n ครั้ง

-  จงเขียนฟังก์ชัน timetable(x) เพื่อแสดงตารางสูตรคูณแม่ x

-  จงเขียนฟังก์ชันเพื่อแสดงกระดานหมากรุกนานาชาติ chess ดังนี้

:: 

    ♜♞♝♛♚♝♞♜
    ♟♟♟♟♟♟♟♟



    ♙♙♙♙♙♙♙♙
    ♖♘♗♕♔♗♘♖

Hint: จาก Week04 ตัวอักขระสำหรับรูปหมากรุกของ Unicode อยู่ในช่วง
``'\u2654'`` ถึง ``'\u265F'`` หรือ ``0x2654`` ถึง ``0x265F``


ฟังก์ชันที่มี ``parameters`` มากกว่า 1
--------------------------------------

**รูปแบบ**

.. code:: python

    def function_name(function_parameters):
        function_body

1. ระบุชื่อ parameters ทุกตัวโดยใช้ชื่อตัวแปร
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

รายชื่อของ parameters แต่ละตัว นั้นจะคั่นด้วย ``','``
ดังรูปแบบตัวอย่างต่อไปนี้

.. code:: python

    def function_name(a, b, c, d):
        function_body

    ชื่อ parameters จะใช้ชื่ออะไรก็ได้ที่ถูกต้องตามกฏการตั้งชื่อตัวแปร
    (identifiers)

**ตัวอย่าง: function definition**

ร้องเพลง happy birthday ให้ name ทั้งหมด n ครั้ง

.. code:: python

    def singbday(name, n):
        for i in range(n):
            happbday(name)

**ตัวอย่าง: function call**

.. code:: python

    singbday('Tom', 20)


2. ระบุ parameter เป็นชื่อเดียว เพื่อเก็บ arguments ทุกค่าที่ส่งมาเป็น ชุดลำดับข้อมูล
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keyword: tuple unpacking function

โดยชุดลำดับข้อมูลนี้จะมีคุณสมบัติเหมือน ``list``
แต่จะไม่สามารถเปลี่ยนแปลงค่าได้ เรียกว่า ``tuple``

**ตัวอย่าง: function definition**

.. code:: python

    def average(*t):
        print( sum(t) / len(t) )

**ตัวอย่าง: function call**

.. code:: python

    average(1, 2, 3, 4, 5, 6)
    average(3, 5, 9, 7)
    average(9)
    average()

**การส่ง list ไปยังฟังก์ชัน tuple unpacking function**

.. code:: python

    a = [ 1, 2, 3, 4, 5, 6, 7 ]
    average( *a )


**EX0501** GPA Report
---------------------

**โจทย์**
งานทะเบียนได้รับมอบหมายให้หารายชื่อนักศึกษาที่มีผลการเรียนต่ำกว่าผลการเรียนเฉลี่ยของทุกคนมากผิดปกติ
ดังนั้นจึงต้องการโปรแกรมที่จะแสดงข้อมูลรหัสนักศึกษาและผลต่างแยกเป็นบรรทัดเพื่อนำมาประกอบการพิจารณา

เจ้าหน้าที่งานทะเบียนจะกรอกจำนวนนักศึกษาก่อน
จากนั้นก็กรอกรหัสนักศึกษาและเกรดเฉลี่ยแยกบรรทัดละคน
โดยรหัสนักศึกษาและเกรดเฉลี่ยคั่นด้วย ``','``

**ตัวอย่างข้อมูลนำเข้า (Input)**

:: 

    5
    61002001,3.00
    61030002,3.00
    61004003,4.00
    61000004,1.22
    61000101,2.50

จะเห็นว่า ผลการเรียนเฉลี่ยรวมของนักศึกษา 5 คนคือ ``2.744``
ดังนั้นรายการนักศึกษาและผลต่างจากเกรดเฉลี่ยรวมจึงเป็นดังนี้
โดยผลต่างมีทศนิยม 2 ตำแหน่ง

:: 

    61000004,1.22 ห่างจาก ผลการเรียนเฉลี่ยรวม 2.744 - 1.22 = 1.52
    61000101,2.50 ห่างจาก ผลการเรียนเฉลี่ยรวม 2.744 - 2.50 = 0.244

**ตัวอย่างข้อมูลส่งออก (Output)**

:: 

    61002001,0.26
    61030002,0.26
    61004003,1.26
    61000004,1.52
    61000101,0.24

**Solution**

.. code:: python

    n = int(input())
    ids = []
    gpas = []

    for i in range(n):
        line = input().split(',')
        ids.append( line[0] )
        gpas.append( float(line[1]) )

    avg = sum(gpas)/len(gpas)

    for i in range(len(ids)):
        print(f'{ids[i]},{abs(gpas[i]-avg):.2f}')


3. ระบุ parameter เป็นชื่อเดียว เพื่อเก็บ arguments ที่ระบุชื่อและค่าหลายชุดได้
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keyword: key-value unpacking function

**หมายเหตุ** เนื้อหาขั้นสูง จำเป็นต้องรู้เรื่อง collection ก่อน

**ตัวอย่าง: function definition**

.. code:: python

    def printkv(**kv):
        print( type(kv) )
        print( kv )

**ตัวอย่าง: function call**

.. code:: python

    printkv(name='Paul Phoenix', age=25, gpa=3.44)


Exercises
---------

-  **EX0502** จงเขียนฟังก์ชัน max3() เพื่อแสดง
   ตัวเลขที่มีค่าที่สูงที่สุด 3 ค่าจาก argument ที่ส่งใน function call
   การแสดงผลต้องเรียงลำดับจากน้อยไปมาก แยกตัวเลขละบรรทัด

**ตัวอย่าง**

+-----------------------+----------+
| Input                 | Output   |
+=======================+==========+
| ``max3(1,2,3,4,5)``   | 345      |
+-----------------------+----------+
| ``max3(2,5,5)``       | 255      |
+-----------------------+----------+
| ``max3(4,5)``         | 45       |
+-----------------------+----------+
| ``max3()``            |          |
+-----------------------+----------+

-  **EX0503** จากโจทย์ **EX0501** จงหา แสดงรายการเป็น ผลต่างยกกำลังสอง

-  **EX0504** จากโจทย์ **EX0503** จงหาผลรวมของผลต่างยกกำลังสองของทุกคน
   แล้วแสดงค่า รากที่สองของผลรวมนั้น

สมการหาค่าเบี่ยงเบนมาตรฐานคือ

.. math::  stdev = \sqrt{\frac{\sum{(gpa_i-avg)^2}}{n-1}} 

เมื่อ

-  :math:`avg` คือ ผลการเรียนเฉลี่ยรวมของทุกคน

-  :math:`(gpa_i - avg)^2` คือ ผลต่างยกกำลังสองของนักศึกษาคนที่
   :math:`i`

-  :math:`n` คือ จำนวนนักศึกษาทั้งหมด

-  **EX0505**
   จงเขียนโปรแกรมเพื่อหาค่าเบี่ยงเบนมาตรฐานของผลการเรียนของนักศึกษาตามรูปแบบข้อมูลนำเข้าข้อ
   **EX0501**


Parameters และอายุการใช้งาน
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ตัวแปรที่ประกาศไว้ในการประกาศฟังก์ชันถือว่าเป็น ตัวแปรของฟังก์ชัน
   (function variable)
-  ตัวแปรที่ประกาศไว้ใน function body ถือว่าเป็น function variable
-  function variable จะมีอายุการใช้งานเฉพาะภายในฟังก์ชันเท่านั้น
-  คำสั่งในฟังก์ชันหนึ่งไม่สามารถอ้างถึงตัวแปรของฟังก์ชันอื่นได้

ขั้นตอนการทำงานเมื่อมีการเรียกใช้ฟังก์ชัน
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**คำสั่ง**

.. code:: python

    def working(x, y):
        z = x**y
        print(z)

    print('Hello world.')
    working(3,5)    
    print('I am done.')

**การทำงาน**

:: 

    print('Hello world.')
    working(3,5) 
    _______________
    _______________ working(x=3, y=5)
    _______________    z = 3**5
    _______________    print(243)
    _______________
    print('I am done.')


ฟังก์ชันที่มีค่าส่งกลับ
-----------------------

มีหลายฟังก์ชันที่ใช้งานมาเป็นฟังก์ชันที่มีค่าส่งกลับเช่น
``input(), math.sqrt(2.5), abs(3.75 - 4.00), sum([1,2,3,4,5])`` เป็นต้น

ฟังก์ชันที่ต้องการส่งค่ากลับให้คนอื่นเรียกใช้ได้จะต้องมีคำสั่ง return
ตามรูปแบบต่อไปนี้

.. code:: python

    def function_name(function_parameters):
        
        function_body
        
        return value

**ตัวอย่างฟังก์ชันที่มีค่าส่งกลับ**

.. code:: python

    def square(x):
        return x*x

**ตัวอย่างการเรียกใช้งานฟังก์ชันที่มีค่าส่งกลับ**

.. code:: python

    square(4)
    print( square(4) )
    x = 5
    print( square(x) )
    n = 9
    print( square(n) )
    y = square(x)
    print( y )
    print( square(x) + square(n) )

.. code:: python

    def root(a, b, c):
        return (-b + math.sqrt(b**2 - 4*a*c))/(2*a)

    def dist(x):
        return ''.join(name.split())


Exercises
---------

-  กำหนดฟังก์ชันในการหาระยะหว่างระหว่างจุด :math:`P_1 = (x_1, y_1)` และ
   :math:`P_2 = (x_2, y_2)` คือ

.. math::


   d = \sqrt{ (x_2 - x_1)^2 - (y_2 - y_1)^2) }

จงเขียนฟังก์ชัน

.. code:: python

    def dist(x1, y1, x2, y2):


ฟังก์ชันที่ส่งกลับมากกว่า 1 ค่า
-------------------------------

รากของสมการ :math:`f(x) = ax^2 + bx +c` มี 2 ค่าได้แก่

:math:`r_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}`

:math:`r_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}`

.. code:: python

    import math

    def roots(a, b, c):
        r = math.sqrt(b**2 - 4*a*c)
        r1 = (-b + r)/(2*a)
        r2 = (-b - r)/(2*a)
        return r1, r2

    a = float(input('กรอกค่า a: '))
    b = float(input('กรอกค่า b: '))
    c = float(input('กรอกค่า c: '))
    x = roots(a, b, c)
    print(f'{x}')

    a = float(input('กรอกค่า a: '))
    b = float(input('กรอกค่า b: '))
    c = float(input('กรอกค่า c: '))
    print(f'{roots(a, b, c)}')

    def solve():
        a = float(input('กรอกค่า a: '))
        b = float(input('กรอกค่า b: '))
        c = float(input('กรอกค่า c: '))
        x = roots(a, b, c)
        print(f'{x}')

    solve()    
    solve()    
    solve()    


Note
----

-  ทุกฟังก์ชันมีค่าส่งกลับ ไม่ว่าจะมีคำสั่ง return หรือไม่ก็ตาม

-  ฟังก์ชันที่ไม่มีคำสั่ง ``return`` จะมีค่าส่งกลับเป็น ``None``

-  argument เป็นค่าที่ส่งไปให้ parameter ในฟังก์ชันได้

-  parameter ของฟังก์ชัน
   สร้างขึ้นตอนถูกเรียกใช้และหายไปเมื่อฟังก์ชันเสร็จสิ้นการทำงาน

-  Python เรียกฟังก์ชัน แบบส่งผ่านค่าไปยัง parameter (pass-by-value)
   ทำให้ **ไม่** สามารถเปลี่ยนแปลงข้อมูลต้นฉบับได้

-  ภาษาโปรแกรมบางภาษา เรียกฟังก์ชัน แบบส่งผ่านค่าอ้างอิงไปให้ parameter
   (pass-by-reference) ทำให้สามารถเปลี่ยนแปลงข้อมูลต้นฉบับได้


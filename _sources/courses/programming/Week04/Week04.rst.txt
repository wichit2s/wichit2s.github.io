โครงสร้างข้อมูลแบบลำดับ
=======================

    Sequences: Strings, Lists, and Files

|Binder| |Download|

    คำสั่งเกี่ยวกับข้อความ

จุดประสงค์
----------

1. อธิบายข้อมูลประเภทข้อความและสามารถเขียนในโปรแกรมได้
2. สามารถใช้งานฟังก์ชันต่างๆสำหรับจัดการข้อความได้
3. เข้าใจหลักการของข้อมูลประเภทลำดับ (sequence) การเข้าถึงสมาชิก
   (indexing) สำหรับข้อมูลประเภทข้อความและ list ได้
4. สามารถ format ข้อความเพื่อการแสดงผลที่ทำความเข้าใจง่ายได้
5. สามารถเขียนคำสั่งเพื่ออ่านและเขียนไฟล์ได้

ข้อมูลประเภท ข้อความ
--------------------

-  *ข้อความ* เป็นประเภทของข้อมูลที่พบและใช้งานบ่อยมากในซอฟต์แวร์ต่างๆ
   เช่น editor word processor หรือ ซอฟต์แวร์สำหรับสำนักงานอื่นๆ
-  *ข้อความ* โดยทั่วไปเรียกว่า string หรือ text สำหรับ Python
   ข้อมูลประเภทนี้เรียกว่า ``str``

.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gl/wichit2s%2Fprogrammingfundamentals/master?filepath=Week04%2FWeek04.ipynb
.. |Download| image:: ../icons/download.png
   :target: https://gitlab.com/wichit2s/programmingfundamentals/raw/master/Week04/Week04.ipynb?inline=false

การประกาศข้อมูลประเภทข้อความใน ``Python``
-----------------------------------------

``str`` เป็นชุดข้อมูลที่เรียกว่า ลำดับของตัวอักขระ (sequence of
characters) อยู่ภายในคู่ของ ``"``\ (double quote) หรือภายในคู่ของ ``'``
(single quote)

*หมายเหตุ* สำหรับ python 3.6+ ``str``
สามารถใช้ตัวแปร(identifier)ร่วมในข้อความได้ ``f'ข้อความ {ตัวแปร}'``

.. code:: python

    name = 'Paul'
    lastname = "Phoenix"
    print("My name is ", name, lastname, '.')
    print(f'My name is {name} {lastname}.')
    text = f"My name is {name} {lastname}."
    print(text)

    type(name)
    type(lastname)
    print( type(text) )
    # <class 'str'>


การรับข้อมูล ประเภท ข้อความ
---------------------------

.. code:: python

    name = input('Please enter your name ')
    lastname = input()
    print(f'Hello, {name} {lastname}.')


การจัดเก็บข้อมูลประเภท *ข้อความ*
--------------------------------

.. figure:: ./images/paul_phoenix.png
   :alt: string representation

   string representation

การเข้าถึงตัวอักขระใน *ข้อความ* โดยใช้ตัวเลขจำนวนเต็มระบุตำแหน่ง
----------------------------------------------------------------

.. code:: python

    name = 'Paul Phoenix'
    len(name) # 12
    name[0]   # 'P'
    name[1]   # 'a'
    name[4]   # ' '


การระบุตำแหน่งจากด้านหลังของ *ข้อความ*
--------------------------------------

.. code:: python

    name[len(name)-3]  # 'n'
    name[len(name)-2]  # 'i'
    name[len(name)-1]  # 'x'

    n = len(name)
    name[n-3]
    name[n-2] 
    name[n-1] 

    name[-3] # 'n'
    name[-2] # 'i'
    name[-1] # 'x'


การตัดกลุ่มของอักขระ (slicing, substring)
-----------------------------------------

.. code:: python

    text[start:end]

-  ``start`` และ ``end`` เป็น ตัวแปร ที่อ้างถึงค่า จำนวนติด

.. code:: python

    name = 'Paul Phoenix'
    name[0:4]   # 'Paul'
    name[5:12]  # 'Phoenix'

-  ถ้าต้องการ ``'Pho'`` จะต้องใช้คำสั่งใด
-  คำสั่งต่อไปนี้ได้อะไร?

   .. code:: python

       start = 2
       end = 6
       print(name[start:end])

   **หมายเหตุ**

-  ผลลัพธ์จะไม่รวมตัวอักขระที่ตำแหน่ง ``end``
-  ``start`` ถ้าเป็น ``0`` ไม่จำเป็นต้องระบุก็ได้

   .. code:: python

       name[0:4]
       name[:4]

-  ``end`` ถ้าเป็น ``len(name)`` ไม่เป็นต้องระบุก็ได้

   .. code:: python

       name[5:len(name)]
       name[5:]

-  ผลลัพธ์ของคำสั่งต่อไปนี้คืออะไร?

   .. code:: python

       name[:]


การนำ *ข้อความ* มาต่อกัน
------------------------

-  โดยใช้เครื่องหมาย ``+``

   .. code:: python

       name = 'Paul'
       lastname = 'Phoenix'
       name + lastname

-  โดยใช้เครื่องหมาย ``*`` กับตัวเลข

   .. code:: python

       name * 3
       4 * lastname

-  แบบผสม

   .. code:: python

       (name * 3) + (5 * lastname)
       (name * 2) + (3 * ' จะไม่เข้าเรียนช้าอีกแล้ว ')


การไล่ดูตัวอักขระใน *ข้อความ* โดยใช้ ``for``
--------------------------------------------

-  แสดงอักขระละบรรทัด

   .. code:: python

       name = 'Paul Phoenix'
       for ch in name:
       print(ch)

-  แสดงทุกอักขระในหนึ่งบรรทัดโดยแยกด้วยช่องว่าง ``','``

   .. code:: python

       name = 'Paul Phoenix'
       for ch in name:
       print(ch, end=',')


ตารางสรุป
---------

.. list-table:: ตารางสรุป
    :widths: 40 60
    :header-rows: 1

    * - ตัวดำเนินการ (Operator)
      - ความหมาย (Meaning)
    * - ``name + lastname``
      - ต่อข้อความด้านซ้ายและขวาเข้าด้วยกัน (Concatenation)
    * - ``3*name`` หรือ ``name*4`` 
      - ต่อข้อความตามจำนวนครั้งที่ระบุด้านซ้ายหรือด้านขวา (Repetition) 
    * - ``name[index]``          
      - การใช้ตัวเลขเพื่อระบุตำแหน่งของอักขระในข้อความ (Indexing)   
    * - ``name[start:end]``       
      - การใช้สองตัวเลขเพื่อตัดข้อความย่อย (Slicing)               
    * - ``len(name)``              
      - จำนวนตัวอักษรในข้อความ (Length)                        
    * - ``for ch in name``         
      - การไล่ดูอักขระในข้อความ (Iteration)                     


การแบ่งข้อความออกเป็นกลุ่ม
--------------------------

-  การแบ่งกลุ่มโดยใช้ slicing

.. code:: python

    days = 'MonTueWedThuFriSatSun'
    print(days[0:3])   # 'Mon'
    print(days[3:6])   # 'Tue'
    print(days[6:9])   # 'Wed'
    print(days[9:12])  # 'Thu'
    print(days[12:15]) # 'Fri'
    print(days[15:18]) # 'Sat'
    print(days[18:21]) # 'Sun'

    print(days[0*3:1*3])   # 'Mon'
    print(days[1*3:2*3])   # 'Tue'
    print(days[2*3:3*3])   # 'Wed'
    print(days[3*3:4*3])   # 'Thu'
    print(days[4*3:5*3])   # 'Fri'
    print(days[5*3:6*3])   # 'Sat'
    print(days[6*3:7*3])   # 'Sun'


**โจทย์** จงเขียนโปรแกรมเพื่อรับตัวเลขจากผู้ใช้แล้วแสดงชื่อวัน

.. list-table:: ตัวอย่างข้อมูล
    :widths: 45 45
    :header-rows: 1

    * - Input
      - Output
    * - 0       
      - Mon
    * - 1        
      - Tue      
    * - 2        
      - Wed      
    * - 3        
      - Thu      
    * - 4        
      - Fri      
    * - 5        
      - Sat      
    * - 6        
      - Sun      

.. code:: python

    days = 'MonTueWedThuFriSatSun'
    n = int(input())
    print(days[n*3:(n+1)*3])


-  การแบ่งกลุ่มโดยระบุอักขระที่ใช้แยก (separator,delimiter) ให้เป็น
   ลำดับ (list)

-  ตัวอย่าง 1 การแบ่งด้วยช่องว่าง ``' '``

   .. code:: python

       DAYS = 'จันทร์ อังคาร พุธ พฤหัสบดี ศุกร์ เสาร์ อาทิตย์'
       days = DAYS.split(' ')
       # ['จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์', 'อาทิตย์']
       n = int(input())
       print(days[n])

-  ตัวอย่าง 2 การแบ่งด้วย comma ``','``

   .. code:: python

       GPA = '3.40,2.55,3.00,3,3.65'
       gpas = GPA.split(',')
       # [ '3.40', '2.55', '3.00', '3', '3.65' ]
       for e in gpas:
       f = float(e)
       print( e, type(e), f, type(f) )


Exercises
---------

-  **EX0401**
   จงเขียนโปรแกรมเพื่อรับประโยคยาวภายในหนึ่งบรรทัดในภาษาอังกฤษจากผู้ใช้แล้วให้ระบุจำนวนคำที่ผู้ใช้กรอก
   โดยแต่ละคำคั่นด้วยช่องว่าง

.. list-table:: ตัวอย่างข้อมูล
    :widths: 40 60
    :header-rows: 1

    * - Input 
      - Output
    * - Hello, Paul                
      - 2
    * - My name is Paul Phoenix.   
      - 5
    * - You are 26 years old.      
      - 5

-  **EX0402**
   จงเขียนโปรแกรมเพื่อรับตัวเลขจากผู้ใช้แล้วแสดงชื่อเดือนตามหมายเลขนั้น
   (เดือนเริ่มจาก 1 เป็น January)

.. list-table:: ตัวอย่างข้อมูล
    :widths: 40 60
    :header-rows: 1

    * - Input 
      - Output
    * - 1       
      - January     
    * - 2       
      - February    
    * - 3       
      - March       
    * - 4       
      - April       
    * - 5       
      - May         
    * - 6       
      - June        
    * - 7       
      - July        
    * - 8       
      - August      
    * - 9       
      - September   
    * - 10      
      - October     
    * - 11      
      - November    
    * - 12      
      - December    

การจัดรูปแบบการแสดงข้อความ
--------------------------

การจัดรูปแบบโดยใช้ ``%``
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    name = 'Paul'
    lastname = 'Phoenix'
    gpa = 3.123456
    print( 'GPA of %s %s is %f' % (name, lastname, gpa) )
    # GPA of Paul Phoenix is 3.123456
    print( 'GPA of %s %s is "%f"' % (name, lastname, gpa) )
    # GPA of Paul Phoenix is "3.123456"
    print( 'GPA of %s %s is "%5.2f"' % (name, lastname, gpa) )
    # GPA of Paul Phoenix is " 3.12"


การจัดรูปแบบโดยใช้ ``format()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    name = 'Paul'
    lastname = 'Phoenix'
    gpa = 0.123456
    print( 'GPA of {} {} is {}'.format(name, lastname, gpa) )
    print( 'GPA of {} {} is {:5.2f}'.format(name, lastname, gpa) )


การจัดรูปแบบโดยใช้ ``f-string`` สำหรับ python 3.6+
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    name = 'Paul'
    lastname = 'Phoenix'
    gpa = 3.123456
    print( f'GPA of {name} {lastname} is {gpa:5.2f}' )


ลำดับกับข้อความ
---------------

ใน Python *ข้อความ* ถือว่าเป็น ลำดับ (sequence)
และสามารถใช้ตัวดำเนินการแบบเดียวกับลำดับประเภทอื่นๆ
ข้อมูลประเภทลำดับ(sequence) ที่พบบ่อยในภาษา Python คือ list
ซึ่งสมาชิกในลำดับจะเป็นข้อมูลประเภทใดก็ได้ แต่โดยปกติแล้วสมาชิกใน list
จะเป็นประเภทเดียวกันเพื่อให้ง่ายต่อการหาข้อผิดพลาดของ code (debug)

-  การประกาศลำดับแบบ list

.. code:: python

    [1, 2, 3, 4, 5, 6]
    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    a = [1, 2, 3, 4, 5, 6]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    type(a)     # <class list>
    type(days)  # <class list>

-  list กับตัวดำเนินการ

   .. code:: python

       [1, 2, 3] + [4, 5, 6]      # [1, 2, 3, 4, 5, 6]
       [1, 2] + [1, 2]            # [1, 2, 1, 2]
       [1, 2] * 3                 # [1, 2, 1, 2, 1, 2]

-  list กับ indexing

   .. code:: python

       a = [1, 2, 3, 4, 5, 6]
       days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
       a[1]                       # 2
       a[2]                       # 3
       a[-1]                      # 6
       days[0]                    # 'Mon'
       days[1]                    # 'Tue'
       days[-1]                   # 'Sun'
       len(a)                     # 6
       len(days)                  # 7
       letters = 'ABCDEF'
       len(letters)               # 6
       letters[0]                 # 'A'
       letters[1]                 # 'B'
       letters[2]                 # 'C'
       letters[-1]                # 'F'

-  list กับ slicing

   .. code:: python

       a = [1, 2, 3, 4, 5, 6]
       days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
       letters = 'ABCDEF'
       a[1:4]                     # [2, 3, 4]
       days[1:4]                  # ['Tue', 'Wed', 'Thu']
       letters[1:4]               # 'BCD'


*ข้อความ* ``str`` ต่างจาก ``list``
----------------------------------

-  **สมาชิกของ ``str`` ไม่สามารถกำหนดค่าใหม่ได้**

.. code:: python

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    letters = 'ABCDEF'
    days[1] = 'Tuesday'
    letters[1] = 'b'
    # TypeError: 'str' object does not support item assignment

-  **Mutable Value** ค่าเปลี่ยนแปลงได้

-  **Immutable Value** ค่าเปลี่ยนแปลงได้


การเข้ารหัสตัวอักขระ
--------------------

-  จำนวนอักขระที่ Python รองรับ
   `Unicode <https://docs.python.org/3/howto/unicode.html>`__ > 100,000
   โดยการเข้ารหัสแบบ UTF-8 ในช่วง ``0`` - ``0x10FFFF``

-  ``ก - ฮ`` อยู่ในช่วง ``0x0E01`` - ``0x0E2E``
-  สระ อยู่ในช่วง ``0x0E30`` - ``0x0E4F``
-  เลขไทย อยู่ในช่วง ``0x0E50`` - ``0x0E59``
-  ``0x0E01`` เป็นจำนวนเต็มใน Python
-  คำสั่งแปลงตัวเลขเป็น ตัวอักขระ ``chr(0x0E01)``

-  **การระบุอักขระ**

.. code:: python

    print('\u0E01')
    print('\u23F0 = ⏰')
    c = 0x23F0
    for i in range(10): 
        print(chr(c+i), end=' ')

-  คำสั่งแปลง ตัวอักขระ เป็น ตัวเลข ``ord('ก')``

.. code:: python

    kor = ord('ก')
    hor = ord('ฮ')
    for i in range(kor, hor):
        print(chr(i), end=' ')


Exercises แสดงอักขระในช่วงต่อไปนี้
----------------------------------

-  ``0x2654`` ถึง ``0x265F``
-  ``0x2660`` ถึง ``0x2667``


ฟังก์ชันที่สำคัญของ ``str``
---------------------------

.. list-table:: ตารางสรุป
    :widths: 40 60
    :header-rows: 1

    * - Function
      - Description
    * - ``s.split(',')``             
      - แยกข้อความเป็น list ด้วย ``','``                                                    
    * - ``s.capitalize()``           
      - ทำให้ตัวอักษรตัวแรกเป็นตัวพิมพ์ใหญ่ ``'paul' -> 'Paul'``                                  
    * - ``s.title()``                
      - ทำให้ตัวอักษรตัวแรกของทุกคำเป็นตัวพิมพ์ใหญ่ paul ``'phoenix' -> 'Paul Phoenix'``           
    * - ``s.center(10)``             
      - ทำให้ให้ข้อความยาว 10 ตัวอักษรและข้อความต้นฉบับอยู่ตรงกลาง ``'paul' -> '   paul   '``      
    * - ``s.ljust(10)``              
      - ทำให้ให้ข้อความยาว 10 ตัวอักษรและข้อความต้นฉบับชิดซ้าย ``'paul' -> 'paul      '``          
    * - ``s.rjust(10)``              
      - ทำให้ให้ข้อความยาว 10 ตัวอักษรและข้อความต้นฉบับชิดขวา ``'paul' -> '       paul'``         
    * - ``s.count('se')``            
      - นับจำนวนข้อความ ``'se'`` ที่ปรากฏอยู่ใน s เช่น ``'These seeds are greased' -> 3``       
    * - ``s.find('se')``             
      - หาตำแหน่งของ ``'se'`` ที่ปรากฏอยู่ใน s จากซ้าย เช่น ``'These seeds are greased' -> 3``  
    * - ``s.rfind('se')``            
      - หาตำแหน่งของ ``'se'`` ที่ปรากฏอยู่ใน s จากขวา เช่น ``'These seeds are greased' -> 20`` 
    * - ``s.join(['AB','CD','EF'])`` 
      - รวมข้อความใน list แล้วคั่นด้วย s เช่น ``':'.join(['AB','CD','EF']) -> ''AB:CD:EF'``    
    * - ``s.lower()``                
      - ข้อความ ``s`` ที่แปลงเป็นตัวพิมพ์เล็กทั้งหมด                                               
    * - ``s.upper()``                
      - ข้อความ ``s`` ที่แปลงเป็นตัวพิมพ์ใหญ่ทั้งหมด                                               
    * - ``s.strip()``                
      - ข้อความ ``s`` ที่เอาช่องว่างด้านหน้าและด้านหลังออก                                        
    * - ``s.lstrip()``               
      - ข้อความ ``s`` ที่เอาช่องว่างด้านหน้าออก                                                 
    * - ``s.rstrip()``               
      - ข้อความ ``s`` ที่เอาช่องว่างด้านหลังออก                                                 


ฟังก์ชันในการเพิ่มสมาชิกใน ``list``
-----------------------------------

.. code:: python

    a = [1, 2, 3, 4]
    a.append(5)
    print(a)          # [1, 2, 3, 4, 5]

-  การเขียนคำสั่งเพื่อรับ ตัวเลขจากผู้ใช้ 5 ตัวเลข เพื่อเก็บไว้ใน
   ``list``

.. code:: python

    a = []
    for i in range(5):
        n = int(input())
        a.append(n)
    print(a)    

-  การเขียนคำสั่งเพื่อรับข้อความตามจำนวนบรรทัดที่ผู้ใช้ระบุมาเก็บไว้ใน
   ``list``

.. code:: python

    a = []
    n = int(input('ระบุจำนวนบรรทัดที่จะกรอก: '))
    for i in range(n):
        line = input()
        a.append(line)
    print(a)    


ตัวอย่างการเขียนโปรแกรมเพื่อหาหลักสูตรที่มีเกรดเฉลี่ยสูงที่สุด
--------------------------------------------------------------

**โจทย์**

มหาวิทยาลัยแห่งหนึ่งต้องการหาหลักสูตรที่มีเกรดเฉลี่ยของนักศึกษาทุกคนในหลักสูตรสูงที่สุด
งานทะเบียนจึงได้รวบรวมเกรดเฉลี่ยของนักศึกษาทุกคนในของทุกหลักสูตรไว้รวมกันโดยข้อมูลของแต่ละหลักสูตรจะอยู่ใน
1 บรรทัด
ซึ่งประกอบไปด้วยเกรดเฉลี่ยของนักศึกษาในหลักสูตรทุกคนและเกรดเฉลี่ยแต่ละค่าคั่นด้วย
comma ``','``
โดยบรรทัดแรกจะเป็นตัวเลขระบุจำนวนหลักสูตรทั้งหมดของมหาวิทยาลัย

จงเขียนโปรแกรมเพื่อหาหลักสูตรที่มีเกรดเฉลี่ยรวมของนักศึกษาสูงที่สุด
ผลลัพธ์ของโปรแกรมจะต้องแสดง เกรดเฉลี่ยของหลักสูตรที่สูงที่สุด

**ตัวอย่าง Input**

::

    3
    2.55, 3.40, 3.55, 2.95, 3.00, 3.25
    3.25, 2.40, 3.55, 3.95, 3.22, 3.53, 3.20, 3.32
    3.45, 3.22, 2.95, 3.95, 2.75, 3.66, 2.99, 3.34

**ตัวอย่าง Output**

::

    3.3024999999999998

**Algorithm**

-  อ่านจำนวนหลักสูตร ``n``
-  สร้าง ``list`` ชื่อ ``all_avg``
   เพื่อเก็บค่าเกรดเฉลี่ยรวมของแต่ละหลักสูตร
-  แต่ละหลักสูตรหาค่าเกรดเฉลี่ยรวม ``avg`` (ทำซ้ำ ``n`` รอบ)
-  อ่านข้อมูลของหลักสูตรทั้งบรรทัด เป็น ``line``
-  แยกข้อมูลใน ``line`` ด้วยตัวอักขระ ``','`` เป็น ``info``
-  แปลงเกรดเฉลี่ยที่เป็น ``str`` ใน ``info`` เป็น ``float``
   แล้วเก็บไว้เพื่อหาค่าเฉลี่ยใน ``list`` ชื่อ ``gpa``
-  หาค่าเฉลี่ยโดยใช้สูตร ``avg = sum(gpa)/len(gpa)``
-  เก็บค่าเฉลี่ย ``avg`` ไว้ใน ``all_avg``
-  หาเกรดเฉลี่ยที่มากที่สุด ``max(all_avg)`` พร้อมแสดงผลลัพธ์

**Implementation**

.. code:: python

    n = int(input())
    all_avg = []
    for i in range(n):
        line = input()
        info = line.split(',')
        gpa = []
        for e in info:
            gpa.append( float(e) )
            
        avg = sum(gpa)/len(gpa)
        all_avg.append(avg)

    print( max(all_avg) )


-  **EX0403**
   จงเขียนโปรแกรมเพื่อหาเกรดเฉลี่ยรวมที่น้อยที่สุดของทุกหลักสูตร


-  **EX0404**
   ถ้าในแต่ละบรรทัดมีชื่อหลักสูตรก่อนเกรดเฉลี่ยของนักศึกษาทุกคนในหลักสูตร
   จงเขียนโปรแกรมหาชื่อหลักสูตรที่มีเกรดเฉลี่ยรวมสูงที่สุด

**ตัวอย่าง Input**

:: 

    3
    Biology, 2.55, 3.40, 3.55, 2.95, 3.00, 3.25
    Computer Science, 3.25, 2.40, 3.55, 3.95, 3.22, 3.53, 3.20, 3.32
    Business Administration, 3.45, 3.22, 2.95, 3.95, 2.75, 3.66, 2.99, 3.34

**ตัวอย่าง Output**

:: 

    Computer Science

**hint** ``list`` มีฟังก์ชัน ``sort()`` สำหรับ
เรียงลำดับข้อมูลจากน้อยไปมาก

.. code:: python

    a = [ [2,'A'], [1,'B'], [3,'C'] ]
    a.sort()   
    print(a)    # [ [1,'B'], [2,'A'], [3,'C'] ]


Multi-line string - ข้อความหลายบรรทัด
-------------------------------------

.. code:: python

    a = """ข้อความหลายบรรทัด
    แต่ละบรรทัดจะแยกด้วย อักขระ \n
    ซึ่งเรียกว่า newline character
    """

    print('''ข้อความหลายบรรทัด
    แต่ละบรรทัดจะแยกด้วย อักขระ \n
    เรียกว่า newline character
    ''')


ไฟล์ข้อมูล (File)
-----------------

-  file เก็บข้อมูลเป็นลำดับไว้ในหน่วยความจำสำรอง
   โดยลำดับข้อมูลนั้นมีหลายประเภท
   แต่โดยส่วนใหญ่แล้วจะเป็นไฟล์ที่เก็บข้อความ (text file)
   นั่นคือเก็บลำดับของอักขระนั่นเอง

-  file เก็บข้อความแบบ multi-line string โดยมี ``'\n'`` แยกบรรทัด เช่น

:: 

    line one
    line two 

    line four

เก็บใน text file เป็น

:: 

    line one\\nline two\\n\\nline four


การอ่านข้อความจากไฟล์ (reading from text file)
----------------------------------------------

-  การอ่านทุกบรรทัดเป็นหนึ่งข้อความ (multi-line string)

.. code:: python

    f = open('data.txt', 'r')
    all_text = f.read()
    print(all_text)
    f.close()

-  การอ่านทีละบรรทัดออกมาเป็น ``list``

.. code:: python

    f = open('data.txt', 'r')
    lines = f.readlines()
    print(lines)
    f.close()

-  การอ่านเพื่อประมวลผลทีละบรรทัด

.. code:: python

    f = open('data.txt', 'r')
    for line in f:
        print(line)
    f.close()


การเขียนข้อความลงไฟล์ (writing to text file)
--------------------------------------------

-  การเขียนข้อความ multi-line string ลงไฟล์

.. code:: python

    lines = """3
    Biology, 2.55, 3.40, 3.55, 2.95, 3.00, 3.25
    Computer Science, 3.25, 2.40, 3.55, 3.95, 3.22, 3.53, 3.20, 3.32
    Business Administration, 3.45, 3.22, 2.95, 3.95, 2.75, 3.66, 2.99, 3.34
    """
    f = open('gpa_data.txt', 'w')  #  open in writing mode
    f.write(lines)
    f.close()

-  การเขียน ``list`` ของข้อความลงไฟล์

.. code:: python

    lines = [ 
        '3',
        'Biology, 2.55, 3.40, 3.55, 2.95, 3.00, 3.25',
        'Computer Science, 3.25, 2.40, 3.55, 3.95, 3.22, 3.53, 3.20, 3.32',
        'Business Administration, 3.45, 3.22, 2.95, 3.95, 2.75, 3.66, 2.99, 3.34'
    ]
    f = open('gpa_data.txt', 'w')  #  open in writing mode
    f.writelines(lines)
    f.close()

-  การเชื่อม ``list`` ของข้อความเป็น multi-line string เพื่อเขียนลงไฟล์

.. code:: python

    lines = [ 
        '3',
        'Biology, 2.55, 3.40, 3.55, 2.95, 3.00, 3.25',
        'Computer Science, 3.25, 2.40, 3.55, 3.95, 3.22, 3.53, 3.20, 3.32',
        'Business Administration, 3.45, 3.22, 2.95, 3.95, 2.75, 3.66, 2.99, 3.34'
    ]
    f = open('gpa_data.txt', 'w')  #  open in writing mode
    f.write( '\n'.join(lines) )
    f.close()


-  **EX0405**
   งานทะเบียนของมหาวิทยาลัยเก็บชื่อหลักสูตรและเกรดเฉลี่ยรายบุคคลไว้ในไฟล์ชื่อ
   'gpa\_data.txt' ตามรูปแบบที่กำหนดในตัวอย่าง input ด้านล่าง
   จงเขียนโปรแกรมแสดงรายชื่อหลักสูตรโดยเรียงจากหลักสูตรที่มีเกรดเฉลี่ยรวมต่ำสุดไปหาหลักสูตรที่มีเกรดเฉลี่ยรวมสูงสุด

**ตัวอย่าง Input ไฟล์ ``gpa_data.txt``**

:: 

    3
    Biology, 2.55, 3.40, 3.55, 2.95, 3.00, 3.25
    Computer Science, 3.25, 2.40, 3.55, 3.95, 3.22, 3.53, 3.20, 3.32
    Business Administration, 3.45, 3.22, 2.95, 3.95, 2.75, 3.66, 2.99, 3.34

**ตัวอย่าง Output**

:: 

    Biology
    Business Administration
    Computer Science


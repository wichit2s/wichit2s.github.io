คำสั่งทำซ้ำ ``for``
===================

https://drive.google.com/file/d/1vm2xK-5ZJFiZ-M9a9eHC7LM7Nf3j4t1Z/view?usp=sharing

จุดประสงค์รายสัปดาห์
--------------------

1. ระบุข้อแตกต่างระหว่างการทำซ้ำแบบ for และ while ได้
2. ใช้คำสั่ง for เพื่อไล่แสดงสมาชิกของ tuple, list และ dict ได้
3. เขียนโปรแกรมแก้ปัญหาโดยใช้การทำซ้ำและ nested loop ได้

ที่มาและความสำคัญ
-----------------

ในการเขียนโปรแกรมโดยส่วนใหญ่จำเป็นต้องเขียนคำสั่งเพื่อทำงานเดิมซ้ำกันหลายๆครั้ง
การใช้คำสั่งทำซ้ำวนไปหลายๆรอบนั้นเรียกว่า Loop

การใช้คำสั่ง Loop มีสองแบบได้แก่

1. แบบที่รู้จำนวนครั้งในการทำซ้ำแน่นอน เรียกว่า definite loop
2. แบบที่ไม่รู้จำนวนครั้งในการทำซ้ำ เรียกว่า indefinite loop
   จำเป็นต้องตั้งเงื่อนไขในการทำงาน
   ถ้าเงื่อนไขในการทำงานเป็นเท็จก็จะหยุดทำงาน

โดยปกติแล้วถ้าเป็นรู้จำนวนครั้งที่ต้องทำงานซ้ำแน่นอนจะใช้คำสั่ง ``for``
แต่ถ้าไม่รู้จำนวนครั้งที่แน่นอนต้องใช้เงื่อนไขตรวจสอบการทำงานจะใช้คำสั่ง
``while``

เนื้อหาสัปดาห์นี้จะเน้น การใช้งานคำสั่ง ``for``


คำสั่งทำซ้ำ ``n`` ครั้ง
-----------------------

.. code:: python

    for i in range(n):
        print(i)

Exercises
----------

**EX1101** เขียนคำสั่งแสดงข้อความ ``hello`` ทั้งหมด ``10`` บรรทัด

**EX1102** เขียนคำสังแสดงข้อความต่อไปนี้

::

        *
        **
        ***
        ****
        *****
        

**EX1103** เขียนคำสั่งแสดงข้อความต่อไปนี้

::

        *****
        ****
        ***
        **
        *
        

**EX1104** เขียนคำสั่งเพื่อรับตัวเลข ``10`` ตัวจากผู้ใช้ มาเก็บไว้ใน
list ชื่อ ``a``

**EX1105** เขียนคำสั่งเพื่อรับตัวเลข ``n`` ตัวจากผู้ใช้ มาเก็บไว้ใน list
ชื่อ ``a`` โดยให้ผู้ใช้ระบุ ค่า ``n``


คำตอบข้อ EX1104
----------------

**โจทย์** เขียนคำสั่งเพื่อรับตัวเลข ``10`` ตัวจากผู้ใช้ มาเก็บไว้ใน list
ชื่อ ``a``

**solution**

.. code:: python

    a = []
    for i in range(10):
        x = int(input())
        a.append(x)

    print(a)    


การไล่ดูสมาชิกของชุดข้อมูล
--------------------------

``tuple``
~~~~~~~~~

.. code:: python

    a = (1,2,3,4,5,6,7)
    for i in a:
        print(i)


``list``
~~~~~~~~

.. code:: python

    a = [3,5,7,9,10,19,17,15]
    for i in a:
        print(i)


Exercises
---------

**EX1106** เขียนคำสั่งเพื่อไล่แสดงสมาชิก ของ tuple
('Andy','Betty','Cathy','Eddy','Franky')

**EX1107** เขียนคำสั่งเพื่อไล่แสดงสมาชิก ของ list [2,4,6,8,10]

**EX1108** เขียนคำสั่งเพื่อไล่แสดงสมาชิกของ list ที่ผู้ใช้กรอกใน 1
บรรทัด เช่น 1,3,4,5,6,7,9

**EX1109** เขียนคำสั่งเพื่อไล่แสดงสมาชิกของ list ที่ผู้ใช้กรอกใน 2
บรรทัด โดยแต่ละบรรทัดมีสมาชิกหลายตัวเลขคั่นด้วย ``,``

**EX1110** เขียนคำสั่งเพื่อไล่แสดงสมาชิกของ list ที่ผู้ใช้กรอกใน ``n``
บรรทัด โดยแต่ละบรรทัดมีสมาชิกหลายตัวเลขคั่นด้วย ``,``


เฉลยข้อ EX1109
--------------

**โจทย์** เขียนคำสั่งเพื่อไล่แสดงสมาชิกของ list ที่ผู้ใช้กรอกใน 2 บรรทัด
โดยแต่ละบรรทัดมีสมาชิกหลายตัวเลขคั่นด้วย ``,``

**ตัวอย่างข้อมูลนำเข้า**

::

    2,3,4,5,6,7
    2,4,7,8,5

**ตัวอย่างข้อมูลส่งออก**

::

    [2,3,4,5,6,7,2,4,7,8,5]

**Solution**

.. code:: python

    a = []
    # อ่านข้อมูลบรรทัดแรก
    line = input()
    strlist = line.split(',')
    intlist = map(int, strlist)
    a.extend(intlist)
    # อ่านข้อมูลบรรทัดที่สอง
    line = input()
    strlist = line.split(',')
    intlist = map(int, strlist)
    a.extend(intlist)
    # แสดงข้อมูล
    print(a)


``dict`` - key, value เป็นข้อมูลพื้นฐาน
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # dictionary
    ages = {
        'Andy': 23,
        'Betsy': 20,
        'Cathy':  21,
        'Dorothy': 23
    }


**การไล่ดูสมาชิกโดยใช้ key**

.. code:: python

    for key in ages.keys():
        print(ages[key])


**การไล่ดูสมาชิกโดยใช้ value**

.. code:: python

    for value in ages.values():
        print(value)


**การไล่ดูสมาชิกโดยใช้ key,value**

-  สำหรับ python2 ใช้คำสั่ง

.. code:: python

    for key,value in ages.iteritems():
        print(key, value)

-  สำหรับ python3 ใช้คำสั่ง

.. code:: python

    for key,value in ages.items():
        print(key, value)


``dict`` - key, value เป็น list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # dictionary ที่มี value เป็น list
    scores = {
        'Andy': [23, 30, 23],
        'Betsy': [20, 22, 25],
        'Cathy':  [19, 25, 21],
        'Dorothy': [23, 25, 25]
    }


**การไล่ดูสมาชิกโดยใช้ key**

.. code:: python

    for key in scores.keys():
        print(scores[key])


**การไล่ดูสมาชิกโดยใช้ value**

.. code:: python

    for value in scores.values():
        print(value)


**การไล่ดูสมาชิกโดยใช้ key,value**

-  สำหรับ python2 ใช้คำสั่ง

.. code:: python

    for key,value in scores.iteritems():
        print(key, value)

-  สำหรับ python3 ใช้คำสั่ง

.. code:: python

    for key,value in scores.items():
        print(key, value)


``dict`` - key, value เป็น dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    students = {
        'Andy': { 'age': 23, 'gpa': 3.39 },
        'Betsy': { 'age': 20, 'gpa': 3.23 },
        'Cathy': { 'age': 21, 'gpa': 3.35 },
        'Dorothy': { 'age': 23, 'gpa': 3.40 },
    }


**การไล่ดูสมาชิกโดยใช้ key**

.. code:: python

    for key in students.keys():
        print(students[key])


**การไล่ดูสมาชิกโดยใช้ value**

.. code:: python

    for value in students.values():
        print(value)


**การไล่ดูสมาชิกโดยใช้ key,value**

-  สำหรับ python2 ใช้คำสั่ง

.. code:: python

    for key,value in students.iteritems():
        print(key, value)

-  สำหรับ python3 ใช้คำสั่ง

.. code:: python

    for key,value in students.items():
        print(key, value)


Exercises
---------

**EX1111** เขียนคำสั่งเพื่อเก็บข้อมูลนักศึกษา ``10`` คน เป็น dictionary
โดยให้ผู้ใช้กรอก ชื่อ และ อายุ เป็นข้อมูลของนักศึกษาแต่ละคน

**EX1112** เขียนคำสั่งเพื่อเก้บข้อมูลนักศึกษา ``n`` คน ตามที่ผู้ใช้ระบุ
เป็น dictionary โดยข้อมูลของนักศึกษาแต่ละคนมี อายุ, เกรดเฉลี่ย และ email
โดยให้ใช้ email เป็น key

**EX1113** เก็บข้อมูล dictionary ของ
รายวิชาในหลักสูตรที่นักศึกษาลงในเทอมนี้ (key ควรเป็นอะไร? value
ควรเป็นอะไร?)

**EX1114** เก็บข้อมูล dictionary ของ เพื่อน ``5`` คน (key ควรเป็นอะไร?
value ควรเป็นอะไร?)


เฉลยข้อ EX1111
--------------

**โจทย์** เขียนคำสั่งเพื่อเก็บข้อมูลนักศึกษา ``10`` คน เป็น dictionary
โดยให้ผู้ใช้กรอก ชื่อ และ อายุ เป็นข้อมูลของนักศึกษาแต่ละคน

**ตัวอย่างข้อมูลนำเข้า**

::

    Andy Adams,20
    Betty Bailey,22
    Cathy Cooper,19
    Dorothy Davies,21
    Eddy Evans,19
    Franky Fox,21
    Georgy Green,20
    Henry Harris,21
    Iggy Isaac,19
    Johny Jacobs,20

**ตัวอย่างข้อมูลส่งออก**

::

    {'Andy Adams': 20, 'Betty Bailey': 22, 'Cathy Cooper': 19, 'Dorothy Davies': 21, 'Eddy Evans': 19, 'Franky Fox': 21, 'Georgy Green': 20, 'Henry Harris': 21, 'Iggy Isaac': 19, 'Johny Jacobs': 20}

**Solution**

.. code:: python

    students = {}
    for i in range(10):
        line = input()
        strlist = line.split(',')
        students[ strlist[0] ] = int(strlist[1])
        
    print(students)    


การใช้คำสั่งเงื่อนไขในคำสั่งทำซ้ำ
---------------------------------

ในกรณีที่ต้องการตั้งเงื่อนไขในการทำงานสำหรับการทำคำสั่งทำซ้ำในแต่ละรอบนั้น
สามารถทำได้ด้วยคำสั่งการซ้อนคำสั่ง if ไว้ภายในคำสั่ง for

**ตัวอย่าง** จงเขียนคำสั่งเพื่อคะแนนของนักศึกษา 10 คน
จากนั้นแสดงเกรดและคะแนนโดยเรียงคะแนนจากมากไปน้อย

**เงื่อนไข เกรด**

+----------------------+--------+
| ช่วงคะแนน            | เกรด   |
+======================+========+
| 0 <= คะแนน < 50      | 'F'    |
+----------------------+--------+
| 50 <= คะแนน < 60     | 'D'    |
+----------------------+--------+
| 60 <= คะแนน < 70     | 'C'    |
+----------------------+--------+
| 70 <= คะแนน < 80     | 'B'    |
+----------------------+--------+
| 80 <= คะแนน <= 100   | 'A'    |
+----------------------+--------+

**ตัวอย่างข้อมูลนำเข้า**

::

    73.45
    66.52
    82.50
    53.37
    79.55
    85.98
    75.75
    78.49
    84.25
    86.22

**ตัวอย่างข้อมูลส่งออก**

::

    A,86.22
    A,85.98
    A,84.25
    A,82.5
    B,79.55
    B,78.49
    B,75.75
    B,73.45
    C,66.52
    D,53.37


**Solution 1**

.. code:: python

    scoregrades = []
    for i in range(10):
        score = float(input())
        grade = 'A'
        if score < 50:
            grade = 'F'
        elif score < 60:
            grade = 'D'
        elif score < 70:
            grade = 'C'
        elif score < 80:
            grade = 'B'
        scoregrades.append( [score, grade] )
            
    sortedscoregrades = sorted(scoregrades, reverse=True)
    for scoregrade in sortedscoregrades:
        print(f'{scoregrade[1]},{scoregrade[0]}')


**Solution 2**

.. code:: python

    def grade(score):
        grade = 'A'
        if score < 50:
            grade = 'F'
        elif score < 60:
            grade = 'D'
        elif score < 70:
            grade = 'C'
        elif score < 80:
            grade = 'B'
        return grade
                    
    scoregrades = []
    for i in range(10):
        score = float(input())
        scoregrades.append( [score, grade(score)] )
            
    sortedscoregrades = sorted(scoregrades, reverse=True)
    for scoregrade in sortedscoregrades:
        print(f'{scoregrade[1]},{scoregrade[0]}')


**Solution 3**

.. code:: python

    def grade(score):
        return 'FDCBA'[sum([1 for i in (50,60,70,80) if score > i ])]
                    
    scoregrades = []
    for i in range(10):
        score = float(input())
        scoregrades.append( [score, grade(score)] )
            
    sortedscoregrades = sorted(scoregrades, reverse=True)
    for scoregrade in sortedscoregrades:
        print(f'{scoregrade[1]},{scoregrade[0]}')


ฟังก์ชัน ``sorted( )``
----------------------

**``sorted()``** เป็นฟังก์ชันที่สามารถใช้ได้เลยใน python หรือเป็น
builtin functions สำหรับ
เรียงสร้างชุดข้อมูลใหม่ที่เกิดจากการเรียงลำดับชุดข้อมูลที่ส่งให้ฟังก์ชัน
โดยชุดข้อมูลใหม่ที่สร้างเป็น ``list``

.. code:: python

    sorted(iterable, *, key=None, reverse=False)

-  iterable :math:`\to` เป็นชุดข้อมูล เช่น tuple, list และ dict
-  key :math:`\to` เป็นฟังก์ชันระบุข้อมูลที่จะนำมาใช้เรียงลำดับ
   ถ้าไม่ระบุจะเรียงโดยใช้ข้อมูลลำดับที่ 0
-  reverse :math:`\to` ถ้าเป็น True เรียงลำดับจากมากไปน้อย ถ้าเป็น False
   หรือไม่ระบุจะเรียงจากน้อยไปมาก

**ตัวอย่างการใช้งาน**

.. code:: python

    s = sorted([5,3,4,5,6,7])
    print(s)

    a = [5,3,4,5,6,7]
    s = sorted(a, reverse=True)
    print(s)


**การเรียงลำดับ list ของ list**

.. code:: python

    students = [
        [ 'Andy',    20, 3.74 ],
        [ 'Betty',   19, 2.95 ],
        [ 'Cathy',   21, 3.25 ],
        [ 'Eddy',    19, 3.75 ],
        [ 'Franky',  20, 3.12 ],
        [ 'Dorothy', 22, 2.97 ]
    ]

    def zero(e): 
        return e[0]

    def one(e): 
        return e[1]

    def two(e): 
        return e[2]

**เรียงลำดับตามชื่อ**

.. code:: python

    s0 = sorted(students, key=zero)

**เรียงลำดับตามอายุ จากมากไปน้อย**

.. code:: python

    s1 = sorted(students, key=one, reverse=True)

**เรียงลำดับตามเกรดเฉลี่ย จากน้อยไปมาก**

.. code:: python

    s2 = sorted(students, key=two)


**การเรียงลำดับ dict**

.. code:: python

    students = {
        'Andy':     3.74,
        'Betty':    2.95,
        'Cathy':    3.25,
        'Eddy':     3.75,
        'Franky':   3.12,
        'Dorothy':  2.97
    }

**การเรียงลำดับ key ของ dict**

.. code:: python

    s = sorted(students.keys())
    print(s)

**การเรียงลำดับ key ตามค่าของ value ใน dict**

.. code:: python

    sortedkeysbyvalue = sorted(students, key=students.get)
    print(sortedkeysbyvalue)


การใช้คำสั่งเงื่อนไขในคำสั่งทำซ้ำ
---------------------------------

**ตัวอย่าง** จงเขียนคำสั่งเพื่อรับข้อมูลนักศึกษา 10 คน
โดยข้อมูลของนักศึกษาแต่ละคนประกอบด้วย ชื่อ,เกรดเฉลี่ย
แล้วโปรแกรมแสดงรายชื่อของนักศึกษาที่มีเกรดเฉลี่ยมากกว่าหรือเท่ากับ 3.5
โดยเรียงลำดับจากมากสุดไปหาน้อยสุด

**ตัวอย่างข้อมูลนำเข้า**

::

    Andy Adams,3.45
    Betty Bailey,3.52
    Cathy Cooper,3.50
    Dorothy Davies,3.37
    Eddy Evans,3.55
    Franky Fox,3.98
    Georgy Green,2.75
    Henry Harris,3.49
    Iggy Isaac,3.25
    Johny Jacobs,3.22

**ตัวอย่างข้อมูลส่งออก**

::

    Franky Fox,3.98
    Eddy Evans,3.55
    Betty Bailey,3.52
    Cathy Cooper,3.50


**Solution**

.. code:: python

    namegpa = {}
    for i in range(10):
        strlist = input().split(',')
        gpa = float(strlist[1])
        if gpa >= 3.50:
            namegpa[strlist[0]] = gpa
            
    sortednamelist = sorted(namegpa, key=namegpa.get, reverse=True)
    for name in sortednamelist:
        print(f'{name},{namegpa[name]}')


การซ้อนคำสั่งทำซ้ำ ``Nested for Loop``
--------------------------------------

นอกจากการซ้อนคำสั่งเงื่อนไขในคำสั่งทำซ้ำแล้ว
เรายังสามารถซ้อนคำสั่งทำซ้ำในคำสั่งทำซ้ำอีกด้วย
ช่วยให้สามารถแก้ปัญหาแบบหลายระดับชั้นได้

.. code:: python

    for i in range(3):
        for j in range(5):
            print(f'i={i}, j={j}', end=' ')
        print('')

**ตัวอย่าง**

.. code:: python

    for i in range(8):
        for j in range(8):
            if i%2 == j%2:
                print('\u2766', end='')
            else:
                print('\u2767', end='')
        print()                


Exercises
---------

**EX1115** จงเขียนโปรแกรมเพื่อเก็บคะแนนของ 3 รายวิชาใน 1 ภาคเรียน
โดยที่แต่ละรายวิชามีข้อมูลคะแนนของนักศึกษาแต่ละคนที่ลงทะเบียนในรายวิชา

**ตัวอย่างข้อมูลนำเข้า**

::

    1144131,Programming Fundamental,5
    Andy,20,22,23,10
    Betty,22,25,22,8
    Cathy,19,27,20,9
    Dorothy,23,30,21,10
    1104111,Discrete Mathematics,3
    Andy,20,22,25,10
    Cathy,19,27,21,9
    Dorothy,23,30,22,10
    1144285,Java Programming,6
    Andy,19,21,25,10
    Betty,21,25,20,9
    Cathy,19,26,20,9
    Dorothy,23,28,21,10
    Eddy,24,29,20,9


**EX1116** จงเขียนโปรแกรมเพื่อหาค่าคะแนนรวมของนักศึกษาแต่ละคนในของ 3
รายวิชาใน 1 ภาคเรียน ตามรูปแบบข้อมูลที่ระบุไว้ในข้อ *EX1115*

**EX1117** จงเขียนโปรแกรมเพื่อหาค่าคะแนนรวมของนักศึกษาแต่ละคนในของ n
รายวิชาใน 1 ภาคเรียน โดยผู้ใช้ระบุจำนวนรายวิชา ``n``

**EX1118** จงเขียนโปรแกรมเพื่อหาค่าคะแนนตามรูปแบบข้อมูลที่ระบุไว้ในข้อ
*EX1115* แล้วแสดงเกรดของนักศึกษาตามรายวิชาจำนวน ``n`` รายวิชา
โดยใช้ช่วงคะแนนตามตาราง

**เงื่อนไข เกรด**

+--------------------+--------+
| ช่วงคะแนน          | เกรด   |
+====================+========+
| 0 <= คะแนน < 50    | 'F'    |
+--------------------+--------+
| 50 <= คะแนน < 60   | 'D'    |
+--------------------+--------+
| 60 <= คะแนน < 70   | 'C'    |
+--------------------+--------+
| 70 <= คะแนน < 80   | 'B'    |
+--------------------+--------+
| 80 <= คะแนน        | 'A'    |
+--------------------+--------+

**ตัวอย่างข้อมูลส่งออก**

::

    Andy
    1104111,B
    1144131,B
    1144285,B
    Betty
    1144131,B
    1144285,B
    Cathy
    1104111,B
    1144131,B
    1144285,B
    Dorothy
    1104111,A
    1144131,A
    1144285,A
    Eddy
    1144131,B
    1144285,A
    Franky
    1144285,B

เฉลยข้อ EX1117
--------------

**โจทย์**

จงเขียนโปรแกรมเพื่อหาค่าคะแนนรวมของนักศึกษาแต่ละคนในของ n รายวิชาใน 1
ภาคเรียน โดยผู้ใช้ระบุจำนวนรายวิชา ``n``

**รูปแบบข้อมูลนำเข้า**

-  บรรทัดแรกระบุจำนวนรายวิชา ``n``
-  ตามด้วยข้อมูลรายวิชา ``n`` วิชา
-  ข้อมูลแต่ละรายวิชาเริ่มด้วยข้อมูลทั่วไป ซึ่งประกอบด้วย
   รหัสวิชา,ชื่อวิชา,จำนวนนักศึกษาที่ลงทะเบียน ``x``
-  ถัดมาอีก ``x`` บรรทัดเป็น ชื่อนักศึกษา และ คะแนนดิบที่ได้ 4 ส่วน
   คั่นด้วย ``,``

**รูปแบบข้อมูลส่งออก**

-  แสดงข้อมูลตามรายชื่อนักศึกษาโดยเรียงลำดับตามชื่อนักศึกษา
-  ข้อมูลของนักศึกษาแต่ละคนประกอบไปด้วยลำดับของรายวิชาทั้งหมดที่ลง
   เรียงตามรหัสรายวิชา
-  ข้อมูลรายวิชาของนักศึกษาประกอบด้วย รายวิชาและคะแนนรวมคั่นด้วย ``,``

**ตัวอย่างข้อมูลนำเข้า**

::

    3
    1144131,Programming Fundamental,5
    Andy,20,22,23,10
    Betty,22,25,22,8
    Cathy,19,27,20,9
    Dorothy,23,30,21,10
    Eddy,20,28,20,10
    1104111,Discrete Mathematics,3
    Andy,20,22,25,10
    Cathy,19,27,21,9
    Dorothy,23,30,22,10
    1144285,Java Programming,6
    Andy,19,21,25,10
    Betty,21,25,20,9
    Franky,20,23,22,10
    Cathy,19,26,20,9
    Dorothy,23,28,21,10
    Eddy,24,29,20,9

**ตัวอย่างข้อมูลส่งออก**

::

    Andy
    1104111,77
    1144131,75
    1144285,75
    Betty
    1144131,77
    1144285,75
    Cathy
    1104111,76
    1144131,75
    1144285,74
    Dorothy
    1104111,85
    1144131,84
    1144285,82
    Eddy
    1144131,78
    1144285,82
    Franky
    1144285,75

**Solution**

.. code:: python

    n = int(input())
    students = {}
    for i in range(n):
        course = input().split(',')
        x = int(course[2])
        for j in range(x):
            strlist = input().split(',')
            name = strlist[0]
            scores = map(int, strlist[1:])
            if name in students.keys():
                students[name][course[0]] = sum(scores)
            else:
                students[name] = {
                    course[0]: sum(scores)
                }
    for name in sorted(students.keys()):
        print(f'{name}')
        for course in sorted(students[name].keys()):
            print(f'{course}: {students[name][course]}')

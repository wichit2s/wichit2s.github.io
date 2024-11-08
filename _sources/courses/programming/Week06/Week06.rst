
การเรียกใช้ชุดคำสั่งเสริม
=========================

    Common Packages

|Binder| |Download|

จุดประสงค์
----------

1. สามารถเลือกใช้ชุดคำสั่งเสริมที่มีอยู่ใน python ได้อย่างเหมาะสม
2. สามารถติดตั้งชุดคำสั่งเสริมอื่นๆ เข้ามาใช้งานได้

.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gl/wichit2s%2Fprogrammingfundamentals/master?filepath=Week06%2FWeek06.ipynb
.. |Download| image:: ../icons/download.png
   :target: https://gitlab.com/wichit2s/programmingfundamentals/raw/master/Week06/Week06.ipynb?inline=false

``datetime``
------------

ชุดคำสั่งเสริมสำหรับจัดการข้อมูลเวลา วัน เดือน ปี

วันที่ ``date``
~~~~~~~~~~~~~~~

-  ชุดข้อมูลสำหรับจัดเก็บ วัน เดือน ปี เป็นตัวเลข จำนวนเต็ม

.. code:: python

    import datetime
    year = 2018
    month = 9
    day = 23
    today = datetime.date(year, month, day)

-  ข้อมูลวันนี้

.. code:: python

    today = datetime.date.today()

-  ข้อมูลวัน เดือน ปี

.. code:: python

    d = today.day
    m = today.month
    y = today.year
    print(f'{y}-{m}-{d}')

-  การกำหนดวันจากข้อความ

.. code:: python

    day = datetime.date.fromisoformat('2018-08-10')

-  การแปลงวันเป็นข้อความ

.. code:: python

    day.isoformat()

**โจทย์ EX0601**
จงเขียนคำสั่งเพื่อสร้างวันที่โดยแสดงเป็นวันเดือนปีเกิดของตัวเอง

**โจทย์ EX0602**
จงเขียนคำสั่งเพื่อสร้างวันที่โดยรับวันเดือนปีเกิดจากผู้ใช้


เวลา ``datetime.time``
~~~~~~~~~~~~~~~~~~~~~~

ข้อมูลเวลาในหนึ่งวัน ประกอบไปด้วย ชั่วโมง(hour), นาที(minute),
วินาที(second), microsecond

.. code:: python

    import datetime
    t = datetime.time()
    t = datetime.time(8, 7, 23)
    print(t.hour, t.minute, t.second, t.microsecond)

**โจทย์ EX0603** จงเขียนคำสั่งเพื่อสร้างเวลา โดยระบุ ชม. นาที วินาที
ตามที่ผู้ใช้กำหนด


วันเวลา ``datetime``
~~~~~~~~~~~~~~~~~~~~

ข้อมูลวันและเวลา ประกอบไปด้วย year, month, day, hour, minute, second,
microsecond

.. code:: python

    import datetime

    dt = datetime.datetime()
    print(dt.year)
    now = datetime.datetime.today()
    now.second

**โจทย์ EX0604** จงเขียนคำสั่งเพื่อสร้างวันเวลา โดยให้ผู้ใช้ระบุ ปี
เดือน วัน ชม. นาที และ วินาที


เวลา ``time``
-------------

ชุดคำสั่งเสริมสำหรับจัดการเรื่องเวลา

.. code:: python

    import time
    t = time.time()
    print( time.gmtime() )
    time.sleep(2)
    print( time.localtime() )
    time.sleep(3)
    print( time.asctime() )

ปฏิทิน ``calendar``
-------------------

ชุดคำสั่งเสริมสำหรับแสดงปฏิทิน

.. code:: python

    import calendar
    cal = calendar.calendar()
    print(cal)


การสุ่ม ``random``
------------------

ชุดคำสั่งเสริมสำหรับการสุ่ม

.. code:: python

    import random
    r = random.randint(1, 90)
    print(r)
    print( random.random() )
    a = [ 'Anna', 'Betty', 'Cathy', 'Dorothy', 'Eddy', 'Freddy', 'Iggy', 'Hiccup' ]
    print( random.choice(a) )
    print( random.choices(a) )
    print( random.shuffle(a) )

ฟังก์ชันสำหรับเรียกใช้งาน

:: 

    random()   seed()   randrange()   gauss()  randint()  shuffle() sample()  uniform()


สถิติ ``statistics``
--------------------

ชุดคำสั่งเสริมสำหรับการคำนวณทางสถิติ

.. code:: python

    import statistics

    gpas = [ 3.22, 3.99, 2.5, 2.4, 3.45, 3,55, 3.5, 3.22, 3.22, 3.98, 3.44 ]
    statistics.mean(gpas)
    statistics.median(gpas)
    statistics.mode(gpas)
    statistics.stdev(gpas)
    statistics.variance(gpas)


``os``
------

ชุดคำสั่งเสริมที่มีฟังก์ชันให้เรียกใช้งานระบบปฏิบัติการ

.. code:: python

    import os
    print( os.environ )
    print( typ(os.environ) )
    print( os.environ['USER'] )
    print( os.environ['HOME'] )
    print( os.getcwd() )
    print( os.getuid() )
    print( os.name )
    os.listdir()
    os.makedirs('myfolder')
    os.removedirs('myfolder')
    os.remove('file.txt')


``sys``
-------

ชุดคำสั่งเสริมสำหรับระบบ

.. code:: python

    import sys

    print(sys.argv)
    print(sys.version)
    sys.exit()


``pickle``
----------

ชุดคำสั่งเสิรมสำหรับบันทึกข้อมูล และ อ่านข้อมูลจากไฟล์

.. code:: python

    import pickle

    a = ['test value','test value 2','test value 3']
    file_Name = "testfile"
    fileObject = open(file_Name,'wb') 
    pickle.dump(a,fileObject)   
    fileObject.close()
    fileObject = open(file_Name,'r')  
    b = pickle.load(fileObject)  
    print( b ) 
    print( a==b )


``subprocess``
--------------

ชุดคำสั่งเสริมสำหรับเรียกโปรแกมอื่นขึ้นมาใช้งาน

.. code:: python

    import subprocess

    subprocess.call( ['firefox', 'www.facebook.com'] )


``http.server``
---------------

ชุดคำสั่งเสริมสำหรับสร้าง web server อย่างง่าย

.. code:: python

    import http.server
    import socketserver

    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


``tkinter``
-----------

ชุดคำสั่งเสริมสำหรับสร้าง GUI (หน้าต่างแสดงผล)

**ตัวอย่างที่ 1**

.. code:: python

    from tkinter import *

    window = Tk()

    window.title("Welcome to LikeGeeks app")

    window.mainloop()

**ตัวอย่างที่ 2**

.. code:: python

    from tkinter import Tk, Label, Button

    class MyFirstGUI:
        def __init__(self, master):
            self.master = master
            master.title("A simple GUI")

            self.label = Label(master, text="This is our first GUI!")
            self.label.pack()

            self.greet_button = Button(master, text="Greet", command=self.greet)
            self.greet_button.pack()

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack()

        def greet(self):
            print("Greetings!")

    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()


การติดตั้งชุดคำสั่งอื่น
-----------------------

-  requests

-  httpie

.. code:: sh

    pip install requests
    pip install httpie

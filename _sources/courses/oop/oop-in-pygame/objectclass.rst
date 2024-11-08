************************************************************
คลาสและอ๊อปเจกต์
************************************************************

ตัวแปรและการสร้างอ๊อปเจกต์
============================================================

1. `pygame.display.set_mode([1200, 800])`_ เป็นคำสั่งสร้าง object ของคลาส `pygame.Surface`_ เพื่อการแสดงหน้าต่างขนาด กว้าง 1200 พิกเซล สูง 800 พิกเซล

.. _pygame.display.set_mode([1200, 800]): https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

.. _pygame.Surface: https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

2. `pygame.time.Clock()`_ เป็นคำสั่งสร้าง object ของคลาสสำหรับจัดการเรื่องเวลาของเกม

.. _pygame.time.Clock(): https://www.pygame.org/docs/ref/time.html#pygame.time.Clock

3. `pygame.image.load('BG.png')`_ เป็นคำสั่งสร้าง object ของคลาส `pygame.Surface`_ จากการโหลดไฟล์ภาพชื่อ **BG.png**

.. _pygame.image.load('BG.png'): https://www.pygame.org/docs/ref/image.html#pygame.image.load

4. `bg.get_rect()`_ ส่งกับ object ของคลาส `pygame.Rect()`_ เป็นสี่เหลี่ยมที่มีข้อมูล topleft และ size ของ `pygame.Surface`_ ที่อ้างอิงถึงด้วยตัวแปร bg

.. _bg.get_rect(): https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect

.. _pygame.Rect(): https://www.pygame.org/docs/ref/rect.html#pygame.Rect


ข้อความ
============================================================

Pygame มีคลาส pygame.font.Font เพื่อช่วยในการนำเข้าและแสดงข้อความ


1. download font

* https://fonts.google.com/noto/specimen/Noto+Serif+Thai?query=Thai

2. เปลี่ยนชื่อไฟล์เป็น ``NotoSerifThai.ttf`` เก็บไว้ใน folder ชื่อ ``fonts``

.. image:: images/pygame02.png


.. literalinclude:: codes/pygame02.py
   :linenos:


เสียง
============================================================

เสียงในเกมจะมีอยู่สองแบบได้แก่เสียงที่เกิดจาก action และเสียงเพลง background โดยจะใช้ pygame.mixer ในการจัดการเรื่องเสียงในเกม

* download เสียงเพลง mp3

https://opengameart.org/sites/default/files/desert_theme.zip


.. literalinclude:: codes/pygame03.py
   :linenos:


ตัวละคร
============================================================

เนื่องจากตัวละครจำเป็นต้องใช้หลายภาพเพื่อเปลี่ยนท่าทางการแสดงผลไปเรื่อย ๆ
ตามจำนวนเฟรมที่ผ่านไปของเกม ดังนั้น pygame จึงสร้างคลาส pygame.sprite.Sprite
มาเพื่อจัดการการแสดงผลตัวละครโดยเฉพาะ

1. download character

* https://opengameart.org/content/temple-run-free-sprite

2. เนื่องจากตัวละครมีความซับซ้อน เพื่อให้สะดวกต่อการเรียกใช้งาน จึงจำเป็นต้องเขียนเป็นคลาสเพื่อจัดการข้อมูลท่าทาง(action) ตำแหน่งบนหน้าจอ(x, y) เฟรม(frame) และเวลาสะสม(deltatime) ของตัวละครดังนี้

.. literalinclude:: codes/pygame04.py
   :linenos:


Exercise
------------------------------------------------------------

* เพิ่มข้อมูล scale ในคลาส Character เพื่อให้สามารถลดพื้นที่การแสดงผลเป็นร้อยละได้เช่น scale = .5 หมายถึง ร้อยละ 50 ของขนาดเดิม โดยใช้คำสั่ง ``pygame.transform.scale``

* ทำให้เปลี่ยนท่าทางไปเรื่อย? Idle - Dead - Jump - Run - Slide 


การตอบสนองต่อผู้เล่น
============================================================

ผู้เล่น pygame สามารถโต้ตอบผ่าน Mouse, Keyboard, touch screen, Joystick หรือ Controller ได้ โดยข้อมูลการโต้ตอบจะอยู่เก็บไว้เป็น object ของคลาส pygame.event.Event

กดปุ่มย้ำ ๆ 
------------------------------------------------------------

.. literalinclude:: codes/pygame05.py


กดปุ่มค้างไว้ 
------------------------------------------------------------

.. literalinclude:: codes/pygame06.py


mouse click
------------------------------------------------------------

การสร้าง effect สำหรับยิงปืนลูกซองในเกม

1. download sprite สำหรับ effect

  * https://opengameart.org/content/alotofimpacts-quick-4-frame-impacts-impacts001-004

2. download เสียงยิงปืนลูกซอง

  * https://opengameart.org/sites/default/files/shots.7z

.. literalinclude:: codes/pygame07.py


Exercise
============================================================

* สร้างโครงงานเกมด้วย pygame

****************************************
Encapsultion
****************************************

จุดประสงค์
========================================

* อธิบายความหมายของ Polymorphism ได้
* อธิบายประเภทต่างๆ ของ Polymorphism ได้
* เขียนคำสั่งเพื่อยกตัวอย่างใน Polymorphism แต่ละประเภทได้
* ใช้หลักการเขียนคำสั่ง Polymorphism เพื่อพัฒนาโครงงานได้

ความหมาย
========================================

คำว่า Polymorphism ในศาสตร์วิทยาการคอมพิวเตอร์ หมายถึง 
หลักการเขียนโปรแกรมเพือ (1) ให้ฟังก์ชันสามารถรองรับข้อมูลนำเข้าได้หลายรูปแบบ 
และ (2) ตัวแปรชื่อเดียวสามารถแทนข้อมูลได้หลายประเภท

ประเภท
========================================

Polymorphism แบ่งออกเป็น 3 ประเภทได้แก่

* Ad hoc Polymorphism
* Parametric Polymorphism
* Subtyping Polymorphism


Ad hoc Polymorphism
========================================

หมายถึง ฟังก์ชัน (function) หรือเครื่องหมาย (operator) ที่รองรับการทำงานหลายแบบ (overloading)

Function Overloading
----------------------------------------

ตัวอย่างฟังก์ชันชื่อ add() ในคลาสชื่อ ScoreKeeper ที่สามารถเรียกรับตัวเลขได้หลายแบบและสามารถรับได้มากกว่า 1 ค่า

.. code-block:: python
  :linenos:

  a = ScoreKeeper('มานะ')
  a.add(80)
  a.add(75.5)
  a.add(90.5)
  print(a.getName(), a.getAverage())

  b = ScoreKeeper('มานี')
  b.add(75, 84.2, 90.8)
  print(b.getName(), b.getAverage())

>>> มานะ 82.0
>>> มานี 83.33333333333333

.. tabs::
  .. tab:: Java

    .. literalinclude:: codes/java/ScoreKeeper.java
       :linenos:
       :language: java
  .. tab:: Python

    .. literalinclude:: codes/python/ScoreKeeper.py
       :linenos:
       :language: python
  .. tab:: C++

    .. literalinclude:: codes/cpp/ScoreKeeper.cpp
       :linenos:
       :language: cpp

Exercise
----------------------------------------

:Ex0601: จงเขียนโปรแกรมเพื่อสร้างประกาศและเรียกใช้ ScoreKeeper เพื่อให้สามารถอ่านและแสดงคะแนนเฉลี่ยของทุกคนจากไฟล์ต่อไปนี้


.. literalinclude:: codes/java/scores.txt
   :name: scorestxt
   :caption: ไฟล์ที่ใช้เก็บคะแนน


.. tabs::

  โปรแกรมสำหรับเรียกใช้งานในแต่ละภาษา

  .. tab:: Java

    .. literalinclude:: codes/java/ScoreKeeperApp.java
       :linenos:
       :language: java

  .. tab:: Python
  
    .. literalinclude:: codes/python/ScoreKeeperApp.py
      :linenos:
      :language: python

  .. tab:: C++

    .. literalinclude:: codes/cpp/ScoreKeeperApp.cpp
      :linenos:
      :language: cpp

:Ex0602: จงเขียนคลาสชื่อ Student เพื่อจัดเก็บข้อมูลผลการเรียนของนักศึกษาแต่ละคน 
         โดยผลการเรียนแต่ละวิชาประกอบไปด้วย จำนวนหน่วยกิต (unit) และเกรด (gpa)
         เช่น วิชาหนึ่งมี 3 หน่วยกิตและได้เกรด 3.50 เป็นต้น
         โปรแกรมจะให้ผู้ใช้กรอกจำนวนบรรทัดของข้อมูลนำเข้า n บรรทัด จากนั้นใน n บรรทัดที่เหลือ
         ผู้ใช้จะกรอกชื่อนักศึกษาพร้อมผลการเรียนได้ 2 รูปแบบคือ 

         1. กรอกเฉพาะชื่อและเกรดในกรณีที่รายวิชานั้นมีจำนวนหน่วยกิตเป็น 3

         2. กรอก ชื่อ,จำนวนหน่วยกิต,เกรด ในกรณีที่จำนวนหน่วยกิตไม่เป็น 3
         
         จงเติมคำสั่งของคลาส Student ให้สมบูรณ์ โดยเลือกใช้ภาษาที่ถนัด

.. literalinclude:: codes/data/input0602.txt
   :name: input0602
   :caption: ตัวอย่างการกรอกข้อมูล

.. literalinclude:: codes/data/output0602.txt
   :name: output0602
   :caption: ตัวอย่างผลลัพธ์ของโปรแกรม

.. tabs::

  โครงสร้างของคำสั่งของแต่ละภาษา

  .. tab:: Java

    .. literalinclude:: codes/java/Ex0602.java
       :linenos:
       :language: java

  .. tab:: Python

    .. literalinclude:: codes/python/Ex0602.py
      :linenos:
      :language: python

  .. tab:: C++

    .. literalinclude:: codes/cpp/Ex0602.cpp
      :linenos:
      :language: cpp

Operator Overloading
----------------------------------------

หมายถึง ฟังก์ชันหรือ operator ที่ทำงานได้หลายแบบ ในหลักการเชิงวัตถุจะช่วยให้สามารถเรียกใช้เครื่องหมายเช่น +, -, \*, / แทนการเรียกใช้ method หรือฟังก์ชันของ object

ตัวอย่างการเขียนคลาส ScoreKeeper ให้สามารถใช้เครื่องหมาย + ได้

.. code-block::  python
    :linenos:

    a = ScoreKeeper('มานะ', 0.0)
    a.add(77.0, 73.0, 80.0)

    b = ScoreKeeper('มานะ', 0.0)
    b.add(79.0, 75.0, 73.5, 80.0)

    c = a + b
    print( c.getName(), c.getAverage() )


ตัวอย่างคำสั่งต่อไปนี้แสดงการเขียนคลาส ScoreKeeper เพื่อให้สามารถใช้เครื่องหมาย + ได้ตามตัวอย่างการใช้งาน 

.. tabs::

  ตัวอย่าง class ScoreKeeper เขียนด้วยภาษาต่างๆ

  .. tab:: Java

    .. warning:: 
      
      ภาษาจาวาไม่รองรับ operator overloading

  .. tab:: Python

    .. literalinclude:: codes/python/ScoreKeeperOp.py
      :language: python
      :linenos:

  .. tab:: C++

    .. literalinclude:: codes/cpp/ScoreKeeperOp.cpp
      :linenos:
      :language: cpp


Exercise
----------------------------------------

:Ex0603: จงปรับคลาส Student ใน Ex0602 เพื่อให้สามารถใช้เครื่องหมาย - ระหว่าง object ของคลาส Student ได้
         และสามารถใช้คำสั่งต่อไปนี้เพื่อสร้างและลบผลการเรียนดังคำสั่งตัวอย่างต่อไปนี้ได้

         .. code-block:: python
            :linenos:

            a = Student('มานะ')
            a.add(3.0)
            a.add(3, 4.0)
            a.add(2, 2.5)
            a.add(2, 4.0)

            b = Student('มานะ')
            b.add(2, 4.0)

            c = a - b
            print( c.getName(), c.getAverage() )

.. literalinclude:: codes/data/output0603.txt
   :name: output0603
   :caption: ตัวอย่างผลลัพธ์ของโปรแกรม

.. tabs::

  โครงสร้างของคำสั่งของแต่ละภาษา

  .. tab:: Java

    .. warning:: 
      
      ภาษาจาวาไม่รองรับ operator overloading

  .. tab:: Python

    .. literalinclude:: codes/python/Ex0603.py
      :linenos:
      :language: python

  .. tab:: C++

    .. literalinclude:: codes/cpp/Ex0603.cpp
      :linenos:
      :language: cpp


Parametric Polymorphism
========================================

หมายถึง คลาสหรือฟังก์ชันที่ (ชื่อเดียว) แต่สามารถระบุประเภทของข้อมูลที่จะรองรับได้ เรียกอีกอย่างว่า generic หรือ template

Function
----------------------------------------

* ตัวอย่างการเขียน Generic Function ชื่อ **setName()** ใน class ScoreKeeper เขียนด้วยภาษา Java และการเรียกใช้

.. tabs::

  .. tab:: Java

    .. literalinclude:: codes/java/GenericFunctionApp.java
      :linenos:
      :language: java

  .. tab:: Python

    .. literalinclude:: codes/python/GenericFunctionApp.py
      :linenos:
      :language: python

  .. tab:: C++

    .. literalinclude:: codes/cpp/GenericFunctionApp.cpp
      :linenos:
      :language: cpp

Exercise
----------------------------------------

:Ex0604: จงปรับฟังก์ชัน add() ในคลาส Student เพื่อให้สามารถรับข้อมูลได้ทั้ง จำนวนเต็ม และ ทศนิยม 

         .. code-block:: java
            :linenos:

            Student a = new Student("มานะ");
            a.add(2);
            a.add(3, 3);
            a.add(3.0, 4.0);
            a.add(2, 4);
            System.out.printf("%s %.2f%n", a.getName(), a.getAverage() );

Class
----------------------------------------

.. tabs::

  ตัวอย่าง class ScoreKeeper ที่เป็น Generic สามารถระบุประเภทข้อมูลของคะแนนได้

  .. tab:: Java

    .. literalinclude:: codes/java/ScoreKeeperGeneric.java
      :linenos:
      :language: java

  .. tab:: Python

    .. literalinclude:: codes/python/ScoreKeeper.py
      :linenos:
      :language: python

  .. tab:: C++

    .. literalinclude:: codes/cpp/ScoreKeeperGeneric.cpp
      :linenos:
      :language: cpp

Exercise
----------------------------------------

:Ex0605: จงปรับคลาส Student เพื่อให้สามารถรับข้อมูลได้ทั้ง จำนวนเต็ม และ ทศนิยม 

         .. code-block:: java
            :linenos:

            Student<Integer> a = new Student<Integer>("มานะ");
            a.add(2);
            a.add(3, 3);
            System.out.printf("%s %.2f%n", a.getName(), a.getAverage() );
            Student<Integer> b = new Student<Integer>("มานี");
            b.add(2.0);
            b.add(3.0, 3.5);
            System.out.printf("%s %.2f%n", b.getName(), b.getAverage() );


Subtyping Polymorphism
========================================

หมายถึง ความสามารถใช้ object ของ subclass แทนตำแหน่งที่ระบุว่าต้องการ object ของ superclass 

Function
----------------------------------------

.. tabs::

  ตัวอย่างฟังก์ชันที่สามารถรับ object ของ subclass ตรงตำแหน่งของ superclass

  .. tab:: Java

    .. literalinclude:: codes/java/SubtypeFunctionApp.java
      :linenos:
      :language: java

  .. tab:: Python

    .. literalinclude:: codes/python/SubtypeFunctionApp.py
      :linenos:
      :language: python

  .. tab:: C++

    .. literalinclude:: codes/cpp/SubtypeFunctionApp.cpp
      :linenos:
      :language: cpp

Exercise
----------------------------------------

:Ex0606: จงประกาศคลาส Hero และ NPC เพื่อให้สามารถเรียกใช้คำสั่งต่อไปนี้ได้

         .. code-block:: java
            :linenos:

            public class GameApp {
              public static void fight(GameCharacter a, GameCharacter b) {
                a.fight(b);
              }
              public static void main(String[] args) {
                Hero batman = new Hero("Batman", 100);
                NPC zbot = new NPC("Zombie", 20);
                System.out.println("batman hp = "+batman.getHP());
                // ผลลัพธ์ "batman hp = 100"
                fight(batman, zbot);
                System.out.println("batman hp = "+batman.getHP());
                // ผลลัพธ์ "batman hp = 80"
              }
            }

Class
----------------------------------------

.. tabs::

  ตัวอย่างการประกาศคลาสที่สามารถรองรับ object ของ subclass ตรงตำแหน่งของ superclass

  .. tab:: Java

    .. literalinclude:: codes/java/SubtypeClassApp.java
      :linenos:
      :language: java

  .. tab:: Python

    .. literalinclude:: codes/python/SubtypeClassApp.py
      :linenos:
      :language: python

  .. tab:: C++

    .. warning:: 
      
      ภาษา C++ ไม่รองรับ template supertype

Exercise
----------------------------------------

:Ex0607: จงประกาศคลาส Hero และ NPC เพื่อให้สามารถเรียกใช้คำสั่งต่อไปนี้ได้

.. code-block:: java
   :linenos:

   public class CharacterApp<T> {
     private T c;
     public CharacterApp(T c) {
       this.c = c;
     }
     public void combat(Character b) {
       c.fight(b);
     }
     public static void main(String[] args) {
       Hero batman = new Hero("Batman", 100, 15);
       Hero superman = new Hero("Superman", 200, 25);
       NPC zbot = new NPC("Zombie", 20);

       CharacterApp<Hero> b = new CharacterApp<>(batman);
       CharacterApp<Hero> s = new CharacterApp<>(superman);
       b.print(); // "Batman HP:100 Damage:15
       b.combat(zbot);
       b.print(); // "Batman HP:80 Damage:15
       b.combat(s);
       b.print(); // "Batman HP:55 Damage:15
     }
   }


numpy
============================================================

NumPy หรือ Numerical Python เป็นชุดคำสั่งเสริมสำหรับการประมวลผลข้อมูลตัวเลขโดยใช้ภาษา Python 
ซึ่งใช้คลาสเพื่อเก็บโครงสร้างข้อมูลหลักคือ `numpy.ndarray <https://numpy.org/doc/stable/reference/arrays.ndarray.html>`_ 
ที่เป็นโครงสร้างข้อมูลที่ช่วยในการจัดการข้อมูลหลายมิติได้มีประสิทธิภาพ และรวดเร็ว 

โดย NumPy มีชุดคำสั่งมากมายที่เกี่ยวข้องกับการทำงานกับข้อมูลตัวเลข `numpy.ndarray <https://numpy.org/doc/stable/reference/arrays.ndarray.html>`_  ดังนี้

การสร้าง Arrays
------------------------------------------------------------

* `numpy.array() <https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy-array>`_: ฟังก์ชันสร้าง array 1 มิติหรือมากกว่า

* `numpy.zeros() <https://numpy.org/doc/stable/reference/generated/numpy.zeros.html>`_, `numpy.ones() <https://numpy.org/doc/stable/reference/generated/numpy.ones.html>`_: ฟังก์ชันสร้าง array ที่มีค่าเป็น 0 ทั้งหมดหรือ 1 ทั้งหมด

* `numpy.arange() <https://numpy.org/doc/stable/reference/generated/numpy.arange.html>`_, `numpy.linspace() <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html>`_: สร้าง array ที่มีลำดับตัวเลข

การทำงานกับ Arrays
------------------------------------------------------------

* การดำเนินการทางคณิตศาสตร์: +, -, *, /, ** เป็นต้น

* `numpy.dot() <https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy-dot>`_: ทำการ dot product ของสอง arrays

* `numpy.transpose() <https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy-transpose>`_, `array.T <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html>`_: สลับแถวกับคอลัมน์ของ array

การจัดการรูปร่างของ Arrays
------------------------------------------------------------

* `numpy.shape <https://numpy.org/doc/stable/reference/generated/numpy.shape.html>`_: แสดงรูปร่างของ array

* `numpy.reshape() <https://numpy.org/doc/stable/reference/generated/numpy.reshape.html>`_: เปลี่ยนรูปร่างของ array

* `numpy.vstack() <https://numpy.org/doc/stable/reference/generated/numpy.vstack.html>`_, `numpy.hstack() <https://numpy.org/doc/stable/reference/generated/numpy.hstack.html>`_: นำ arrays มาต่อกันในแนวแถวหรือคอลัมน์

การเข้าถึงข้อมูลใน Arrays
------------------------------------------------------------

* ใช้ index เพื่อเข้าถึงข้อมูลใน array

* การใช้ slicing เพื่อดึงข้อมูลบางส่วนของ array

การทำงานทางคณิตศาสตร์
------------------------------------------------------------

* `numpy.mean() <https://numpy.org/doc/stable/reference/generated/numpy.mean.html>`_, `numpy.sum() <https://numpy.org/doc/stable/reference/generated/numpy.sum.html>`_, `numpy.min() <https://numpy.org/doc/stable/reference/generated/numpy.min.html>`_, `numpy.max() <https://numpy.org/doc/stable/reference/generated/numpy.max.html>`_: คำนวณค่าเฉลี่ย, ผลรวม, ค่าน้อยสุด, และค่ามากสุด

* `numpy.median() <https://numpy.org/doc/stable/reference/generated/numpy.median.html>`_, `numpy.std() <https://numpy.org/doc/stable/reference/generated/numpy.std.html>`_: คำนวณค่ามัธยฐานและส่วนเบี่ยงเบนมาตรฐาน

การทำงานกับ Logical Arrays
------------------------------------------------------------

* `numpy.logical_and() <https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html>`_, `numpy.logical_or() <https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html>`_, `numpy.logical_not() <https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html>`_: การทำงานกับ logical arrays

การสุ่มข้อมูล
------------------------------------------------------------

* `numpy.random.rand() <https://numpy.org/doc/stable/reference/generated/numpy.random.rand.html>`_, `numpy.random.randn() <https://numpy.org/doc/stable/reference/generated/numpy.random.randn.html>`_: สร้างตัวเลขสุ่มจากการกระจายแบบuniform หรือแบบ normal distribution

การทำงานกับตัวเลขทศนิยม
------------------------------------------------------------

* `numpy.round() <https://numpy.org/doc/stable/reference/generated/numpy.round.html>`_, `numpy.floor() <https://numpy.org/doc/stable/reference/generated/numpy.floor.html>`_, `numpy.ceil() <https://numpy.org/doc/stable/reference/generated/numpy.ceil.html>`_: การปัดเศษ

การทำงานกับตัวหนังสือ
------------------------------------------------------------

* `numpy.char.add() <https://numpy.org/doc/stable/reference/generated/numpy.char.add.html>`_, `numpy.char.upper() <https://numpy.org/doc/stable/reference/generated/numpy.char.upper.html>`_, `numpy.char.split() <https://numpy.org/doc/stable/reference/generated/numpy.char.split.html>`_: การทำงานกับข้อมูลตัวหนังสือ


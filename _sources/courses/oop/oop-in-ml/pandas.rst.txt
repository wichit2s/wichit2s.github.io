pandas
============================================================

Pandas เป็นชุดคำสั่งที่ใช้สำหรับการจัดการและวิเคราะห์ข้อมูลด้วยภาษา Python 
โดยมีคลาสสำหรับแทนโครงสร้างข้อมูลหลักคือ `pandas.Series <https://pandas.pydata.org/docs/reference/series.html>`_ และ `pandas.DataFrame <https://pandas.pydata.org/docs/reference/frame.html>`_

ซึ่งเป็นโครงสร้างข้อมูลที่สามารถจัดการข้อมูลในแนวตั้งและตารางตามลำดับ 

การสร้าง DataFrame
------------------------------------------------------------

* `pandas.DataFrame() <https://pandas.pydata.org/docs/reference/frame.html>`_: สร้าง DataFrame จากข้อมูลที่มีอยู่ เช่น list, dictionary, numpy array, หรือ DataFrame อื่น ๆ

* `pandas.read_csv() <https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv>`_, `pandas.read_excel() <https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel>`_: โหลดข้อมูลจากไฟล์ CSV หรือ Excel เพื่อสร้าง DataFrame

การทำงานกับข้อมูล:
------------------------------------------------------------

* `DataFrame.head() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html>`_, `DataFrame.tail() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html>`_: แสดงข้อมูลหัวหรือท้ายของ DataFrame

* `DataFrame.info() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html>`_, `DataFrame.describe() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>`_: แสดงข้อมูลเกี่ยวกับรายละเอียดของ DataFrame

* `DataFrame.shape <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html>`_: แสดงรูปร่างของ DataFrame

* `DataFrame.columns <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html>`_: แสดงชื่อคอลัมน์ของ DataFrame

การเข้าถึงข้อมูลใน DataFrame:
------------------------------------------------------------

ใช้ชื่อคอลัมน์หรือ index เพื่อเข้าถึงข้อมูลใน DataFrame

* `DataFrame.loc[] <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html>`_, `DataFrame.at[] <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html>`_: เข้าถึงข้อมูลด้วย label หรือตำแหน่ง index

การทำงานกับข้อมูลทั่วไป:
------------------------------------------------------------

* `DataFrame.drop() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html>`_: ลบแถวหรือคอลัมน์จาก DataFrame

* `DataFrame.rename() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html>`_: เปลี่ยนชื่อแถวหรือคอลัมน์

* `DataFrame.sort_values() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html>`_: เรียงลำดับข้อมูลตามค่าของคอลัมน์

การทำงานกับข้อมูลทางสถิติ:
------------------------------------------------------------

* `DataFrame.mean() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html>`_, `DataFrame.sum() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html>`_, `DataFrame.min() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html>`_, `DataFrame.max() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html>`_: คำนวณค่าเฉลี่ย, ผลรวม, ค่าน้อยสุด, และค่ามากสุด

* `DataFrame.median() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html>`_, `DataFrame.std() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html>`_: คำนวณค่ามัธยฐานและส่วนเบี่ยงเบนมาตรฐาน

การกระทำกับข้อมูลแบบกำหนดเงื่อนไข:
------------------------------------------------------------

* `DataFrame[condition] <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html>`_: กรองข้อมูลตามเงื่อนไขที่กำหนด

* `DataFrame.isnull() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html>`_, `DataFrame.notnull() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notnull.html>`_: ตรวจสอบข้อมูลที่เป็นค่าว่าง

* `DataFrame.isna() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html>`_, `DataFrame.notna() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html>`_: ตรวจสอบตำแหน่งไม่มีข้อมูล

การทำงานกับข้อมูลที่มีหลายตาราง:
------------------------------------------------------------

* `pandas.concat() <https://pandas.pydata.org/docs/reference/api/pandas.concat.html>`_: นำ DataFrame มาต่อกันในแนวแถวหรือคอลัมน์

* `pandas.merge() <https://pandas.pydata.org/docs/reference/api/pandas.merge.html>`_: รวมข้อมูลจากตารางต่าง ๆ ด้วยคอลัมน์ที่กำหนด

การจัดการข้อมูลที่มีวันที่ (Datetime):
------------------------------------------------------------

* `DataFrame.resample() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html>`_: ทำการ resample ข้อมูลที่มีวันที่

* `DataFrame.groupby() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html>`_: แบ่งข้อมูลตามกลุ่มที่กำหนด

การสร้างและจัดการข้อมูลที่มีคอลัมน์ที่มีค่าเป็น Category:
------------------------------------------------------------

* `DataFrame.astype() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html>`_: เปลี่ยนประเภทของข้อมูล

* `DataFrame.groupby() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html>`_: ใช้ในการจัดกลุ่มข้อมูลที่เป็น category


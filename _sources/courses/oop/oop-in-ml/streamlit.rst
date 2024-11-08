`streamlit`
============================================================

streamlit เป็นชุดคำสั่งเสริมสำหรับภาษา Python ที่ใช้แนวคิดเชิงวัตถุสำหรับการสร้างเว็บแอปพลิเคชัน (web applications) โดยไม่ต้องมีความรู้ด้านการพัฒนาเว็บเลย ช่วยให้สามารถสร้างเว็บแอปพลิเคชันที่สามารถโต้ตอบกับผู้ใช้ได้ในเวลาอันสั้น

การแสดงข้อมูล
------------------------------------------------------------

* `st.write() <https://docs.streamlit.io/library/api-reference/write-magic/st.write>`_: ใช้สำหรับแสดงข้อมูลต่าง ๆ บนเว็บแอปพลิเคชัน

* `st.title() <https://docs.streamlit.io/library/api-reference/text/st.title>`_, `st.header() <https://docs.streamlit.io/library/api-reference/text/st.header>`_, `st.subheader() <https://docs.streamlit.io/library/api-reference/text/st.subheader>`_: ใช้สำหรับแสดงข้อความที่เป็นหัวเรื่อง

การแสดงรูปภาพและวิดีโอ
------------------------------------------------------------

* `st.image() <https://docs.streamlit.io/library/api-reference/media/st.image>`_: ใช้สำหรับแสดงรูปภาพ

* `st.video() <https://docs.streamlit.io/library/api-reference/media/st.video>`_: ใช้สำหรับแสดงวิดีโอ

การรับข้อมูลจากผู้ใช้
------------------------------------------------------------

* `st.button() <https://docs.streamlit.io/library/api-reference/widgets/st.button>`_: สร้างปุ่ม

* `st.text_input() <https://docs.streamlit.io/library/api-reference/widgets/st.text_input>`_, `st.number_input() <https://docs.streamlit.io/library/api-reference/widgets/st.number_input>`_, `st.date_input() <https://docs.streamlit.io/library/api-reference/widgets/st.date_input>`_: สร้างช่องป้อนข้อมูลข้อความ, ตัวเลข, และวันที่

* `st.selectbox() <https://docs.streamlit.io/library/api-reference/widgets/st.selectbox>`_, `st.multiselect() <https://docs.streamlit.io/library/api-reference/widgets/st.multiselect>`_: สร้างกล่อง dropdown และ multi-select dropdown

การเขียนโค้ด Markdown:
------------------------------------------------------------

* `st.markdown() <https://docs.streamlit.io/library/api-reference/text/st.markdown>`_: ใช้สำหรับแสดงข้อความที่ใช้ไฟล์ `Markdown <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>`_

การสร้างกราฟ
------------------------------------------------------------

* `st.line_chart() <https://docs.streamlit.io/library/api-reference/charts/st.line_chart>`_, `st.bar_chart() <https://docs.streamlit.io/library/api-reference/charts/st.bar_chart>`_, `st.area_chart() <https://docs.streamlit.io/library/api-reference/charts/st.area_chart>`_: ใช้สำหรับสร้างกราฟเส้น, กราฟแท่ง, และกราฟพื้นที่

การเรียกใช้ฟังก์ชันหลังจากการเปลี่ยนแปลง
------------------------------------------------------------

* `st.button().on_click() <https://docs.streamlit.io/library/api-reference/widgets/st.button>`_: ใช้สำหรับระบุฟังก์ชันที่จะเรียกเมื่อปุ่มถูกคลิก

การจัดหน้าเว็บแอปพลิเคชัน
------------------------------------------------------------

* `st.sidebar <https://docs.streamlit.io/library/api-reference/layout/st.sidebar>`_: ใช้สำหรับเพิ่มส่วน sidebar ที่ใช้เก็บวิดเจ็ตหรือข้อมูลเสริม

* `st.columns() <https://docs.streamlit.io/library/api-reference/layout/st.columns>`_: ใช้สำหรับแบ่งหน้าจอเป็นคอลัมน์

* `st.tabs() <https://docs.streamlit.io/library/api-reference/layout/st.tabs>`_: ใช้สำหรับแบ่งหน้าจอเป็นแทป

* `st.expander() <https://docs.streamlit.io/library/api-reference/layout/st.expander>`_: ใช้สำหรับขยายพื้นที่แสดงผล

* `st.container() <https://docs.streamlit.io/library/api-reference/layout/st.container>`_: ใช้สำหรับจัดกลุ่มแสดงผล

* `st.empty() <https://docs.streamlit.io/library/api-reference/layout/st.empty>`_: ใช้สำหรับแสดงพื้นที่เปล่า


การใช้ Session State
------------------------------------------------------------

* `st.session_state <https://docs.streamlit.io/library/api-reference/session-state>`_: ใช้สำหรับเก็บข้อมูลที่ต้องการให้เก็บไว้ระหว่าง session


การบันทึกข้อมูล:
------------------------------------------------------------

* `st.cache_data() <https://docs.streamlit.io/library/advanced-features/caching>`_: ใช้สำหรับบันทึกข้อมูลที่ถูกประมวลผลเพื่อลดเวลาการโหลดข้อมูลใน session ถัดไป


ตัวอย่าง
------------------------------------------------------------

* ตัวอย่างที่ 1

.. literalinclude:: code/streamlit/app01.py

* ตัวอย่างที่ 2

.. literalinclude:: code/streamlit/app02.py

* ตัวอย่างที่ 3

.. literalinclude:: code/streamlit/app03.py

* ตัวอย่างที่ 4

.. literalinclude:: code/streamlit/app04.py

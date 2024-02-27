สิ่งที่ควรรู้ก่อนไปต่อ
============================================================

สร้างสภาพแวดล้อม ชื่อ myvenv
------------------------------------------------------------

1. ด้วย venv

.. code-block:

   python3 -m venv myvenv

2. ด้วย conda

.. code-block:

   conda create -n myvenv python=3.10

* เปิดใช้งานสภาพแวดล้อม

  1. ด้วย venv 

    % windows

      ./myvenv/bin/activate

    % macos linux

      source ./myvenv/bin/activate


  2. ด้วย conda

    conda activate myvenv

* ติดตั้งชุดคำสั่งเสริมเพิ่มเติม ชื่อ streamlit


  1. ด้วย venv

    pip install streamlit


  2. ด้วย conda

    conda install streamlit

* ปิดใช้งานสภาพแวดล้อม 

  1. ด้วย venv

    % windows
    ./myvenv/bin/deactivate

    % macos linux
    deactivate



  2. ด้วย conda

    conda deactivate

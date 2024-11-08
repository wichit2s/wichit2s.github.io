diffusers
============================================================

Diffusers เป็นชุดคำสั่งสำหรับจัดการโมเดลการเรียนรู้ของเครื่องที่ฝึกสอนมาเพื่อแปลงข้อความเป็นภาพหรือรูปแบบอื่น ๆ
ที่สามารถนำไปใช้งานในงานที่ต้องการข้อมูลที่มีลักษณะภาพ นอกจากนี้ diffusers ยังช่วยในการฝึกสอนโมเดลเองเพื่อให้สามารถใช้ในงานเฉพาะทางได้อีกด้วย
ซึ่งถ้าต้องการพัฒนาโมเดลใหม่จะใช้แนวคิดในการสืบทอดคุณสมบัติของคลาส `diffusers.ModelMixin <https://huggingface.co/docs/diffusers/main/en/api/models>`_ และ override ฟังก์ชันหลักได้แก่ forward(), from_pretrained() และ save_pretrained() เป็นต้น โดยมีตัวอย่างคลาสและการใช้งานดังนี้

การติดตั้ง
------------------------------------------------------------

เนื่องจากโมเดลในการสร้างภาพถูกฝึกให้เรียนรู้ภาพจำนวนมากทำให้มีขนาดใหญ่และต้องใช้ชุดคำสั่งเสริมที่จำเป็นอื่น ๆ อีกมากมาย ซึ่งที่ขาดไม่ได้คือชุดคำสั่งสำหรับสร้างโมเดลโครงสร้างเครือข่ายปราสาทเทียมและการเรียนรู้เชิงลึก `PyTorch <https://pytorch.org/>`_

.. code-block:: bash

   pip install --upgrade diffusers[torch]


ตัวอย่างการใช้งาน
------------------------------------------------------------

.. code-block::

   from diffusers import DDPMScheduler, UNet2DModel
   from PIL import Image
   import torch

   scheduler = DDPMScheduler.from_pretrained("google/ddpm-cat-256")
   model = UNet2DModel.from_pretrained("google/ddpm-cat-256").to("cuda")
   scheduler.set_timesteps(50)

   sample_size = model.config.sample_size
   noise = torch.randn((1, 3, sample_size, sample_size), device="cuda")
   input = noise

   for t in scheduler.timesteps:
       with torch.no_grad():
           noisy_residual = model(input, t).sample
           prev_noisy_sample = scheduler.step(noisy_residual, t, input).prev_sample
           input = prev_noisy_sample

   image = (input / 2 + 0.5).clamp(0, 1)
   image = image.cpu().permute(0, 2, 3, 1).numpy()[0]
   image = Image.fromarray((image * 255).round().astype("uint8"))
   image_data


ตัวอย่างการใช้งาน pre_trained
------------------------------------------------------------

ตัวอย่างที่ 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block::

   from diffusers import StableDiffusionPipeline
   import torch

   model_id = "runwayml/stable-diffusion-v1-5"
   pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
   #pipe = pipe.to("cuda")

   prompt = "a photo of an astronaut riding a horse on mars"
   image = pipe(prompt).images[0]  
       
   image.save("astronaut_rides_horse.png")




ตัวอย่างที่ 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: code/diffusers/app01.py

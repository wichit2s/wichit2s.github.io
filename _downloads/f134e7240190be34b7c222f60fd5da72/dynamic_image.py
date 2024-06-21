from django.http import HttpResponse
from PIL import Image, ImageDraw   

def pil(req):  
    img = Image.new('RGB', (100,50))
    drawer = ImageDraw.Draw(img)
    drawer.text((10,10), '1145005 Web Dev', fill=(100,250,120))  
    del drawer
    response = HttpResponse(content_type="image/png")  
    img.save(response, 'PNG')  
    return response

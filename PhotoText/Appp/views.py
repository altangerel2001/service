from django.http import JsonResponse
import pytesseract
from PIL import Image
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def extract_text_from_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         image_file = request.FILES['image']
        
#         # Open the image file
#         image = Image.open(image_file)
        
#         # Use Tesseract to extract text from the image
#         extracted_text = pytesseract.image_to_string(image)
        
#         return JsonResponse({'extracted_text': extracted_text})
#     else:
#         return JsonResponse({'error': 'Please provide an image file.'}, status=400)

import base64
from django.http import JsonResponse
import pytesseract
from PIL import Image
import io
import json

# 



from django.http import JsonResponse
from PIL import Image
import pytesseract

# def extract_text_from_image(request):
#     # Replace 'path_to_your_image' with the actual path to your image file
#     image_path = 'C:\\Users\\MU207-14\\Downloads\\ssss.jpg'
#     try:
#         # Open the image file
#         image = Image.open(image_path)
        
#         # Process the image
#         text = pytesseract.image_to_string(image)
        
#         return JsonResponse({'text': text})
#     except FileNotFoundError:
#         return JsonResponse({'error': 'Image file not found'}, status=400)


import base64

with open('C:/Users/MU207-14/Downloads/ssss.jpg', 'rb') as image_file:
    base64_encoded_image = base64.b64encode(image_file.read())

print(base64_encoded_image.decode('utf-8'))


import base64
from django.http import JsonResponse
import pytesseract
from PIL import Image
import io

@csrf_exempt
def extract_text_from_image(request):

    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            base64_encoded_image_data = json_data.get('image')
            
            if base64_encoded_image_data:
                decoded_image_data = base64.b64decode(base64_encoded_image_data)
                image = Image.open(io.BytesIO(decoded_image_data))
                extracted_text = pytesseract.image_to_string(image)
                
                return JsonResponse({'extracted_text': extracted_text})
            else:
                return JsonResponse({'error': 'Base64 encoded image data not provided in JSON request.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Please provide a POST request.'}, status=400)

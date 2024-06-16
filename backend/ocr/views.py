from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from decouple import config, Csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import pytesseract
import fitz

class OCRView(APIView):
    API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-large-handwritten"
    HEADERS = {"Authorization": f"Bearer {config('HUGGING_FACE_API_KEY')}"}

    # def post(self, request, *args, **kwargs):
    #     try:
    #         # Check if 'image' key is present in request.FILES
    #         if 'image' not in request.FILES:
    #             return Response({'error': 'No image file provided'}, status=400)

    #         # Get the image from the request
    #         image = request.FILES['image']

    #         # Convert the image to binary data
    #         if not isinstance(image, InMemoryUploadedFile):
    #             return Response({'error': 'Invalid image file provided'}, status=400)

    #         file_data = image.read()

    #         # Make the API call
    #         response = requests.post(self.API_URL, headers=self.HEADERS, data=file_data)
            
    #         # Check if the API call was successful
    #         if response.status_code == 200:
    #             # Return the API response as JSON
                
    #             return Response({'text':response.json()[0]['generated_text']}, status=200)
    #         else:
    #             # Return an error response if the API call failed
    #             return Response({"error": "Failed to process the image"}, status=response.status_code)

    #     except Exception as e:
    #         # Handle any exceptions that may occur
    #         return Response({"error": str(e)}, status=500)

    def post(self, request, *args, **kwargs):
        try:
            # Check if 'file' key is present in request.FILES
            if 'file' not in request.FILES:
                return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the file from the request
            file = request.FILES['file']

            # Convert the file to binary data
            if not isinstance(file, InMemoryUploadedFile):
                return Response({'error': 'Invalid file provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the file is an image (JPG, PNG) or a PDF
            if file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Image processing using pytesseract
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
            elif file.name.lower().endswith('.pdf'):
                # PDF processing using PyMuPDF
                pdf_document = fitz.open(file)
                text = ""
                for page_number in range(pdf_document.page_count):
                    page = pdf_document[page_number]
                    text += page.get_text()

            else:
                return Response({'error': 'Unsupported file format'}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'text': text}, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle any exceptions that may occur
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
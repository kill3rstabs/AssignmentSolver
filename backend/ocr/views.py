from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import pytesseract
import pymupdf
from decouple import config
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from drf_yasg import openapi
from PyPDF2 import PdfReader

class OCRView(APIView):
    API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-large-handwritten"
    HEADERS = {"Authorization": f"Bearer {config('HUGGING_FACE_API_KEY')}"}

    parser_classes = (MultiPartParser,)


    @swagger_auto_schema(operation_description='Upload file...',)
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            try:
                # Convert the file to binary data
                if not isinstance(file, InMemoryUploadedFile):
                    return Response({'error': 'Invalid file provided'}, status=status.HTTP_400_BAD_REQUEST)

                # Check if the file is an image (JPG, PNG) or a PDF
                if file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # Image processing using pytesseract
                    img = Image.open(file)
                    text = pytesseract.image_to_string(img)

                elif file.name.lower().endswith('.pdf'):
                    # PDF processing using PyPDF2
                    pdf_reader = PdfReader(file)
                    text = ""
                    
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()


                else:
                    return Response({'error': 'Unsupported file format'}, status=status.HTTP_400_BAD_REQUEST)
                
                return Response({'text': text}, status=status.HTTP_200_OK)

            except Exception as e:
                # Handle any exceptions that may occur
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

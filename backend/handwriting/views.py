from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import convert_handwriting, encode_to_base64, read_pdf_file
import os
class HandwritingAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            text = request.data.get('text', '')  # Use request.data for DRF
            file_name = convert_handwriting(text)
            pdf_bytes = read_pdf_file(file_name)
            encoded_pdf = encode_to_base64(pdf_bytes)
            os.remove(file_name)
            return Response({'success': True, 'pdf': encoded_pdf})
        
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response({'success': False, 'error': 'Only POST requests are allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

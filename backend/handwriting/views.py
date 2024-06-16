from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import convert_handwriting
from .utils import encode_to_base64
from .utils import read_pdf_file

class HandwritingAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            text = request.data.get('text', '')  # Use request.data for DRF
            file_name = convert_handwriting(text)
            file_path = '/' + file_name  # Replace with your actual file path
            pdf_bytes = read_pdf_file(file_path)
            base64_pdf = encode_to_base64(pdf_bytes)
            return Response({'base64_pdf': base64_pdf}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response({'success': False, 'error': 'Only POST requests are allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

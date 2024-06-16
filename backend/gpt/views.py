# views.py

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import query  # Import the query function from utils.py

class ChatView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, World!'})

    def post(self, request, *args, **kwargs):
        # Extract user input from request data
        user_input = request.data.get('user_message')

        # Check if user input is not None
        if user_input:
            # Call the query function with user input
            output = query({
                "inputs": user_input,
            })

            # Do something with the 'output' variable or return a response
            return Response({'answer': output[0]["generated_text"]})
        else:
            return Response({'error': 'user_message is required in the request data'})

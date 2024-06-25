# views.py

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import query  # Import the query function from utils.py
import json
from llamaapi import LlamaAPI
from decouple import config
# Initialize the SDK
llama = LlamaAPI(config('LLAMA_API_KEY'))



class ChatView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, World!'})

    def post(self, request, *args, **kwargs):
        try:
            # Extract user input from the request
            user_input = request.data.get('user_message')
            if not user_input:
                return JsonResponse({"error": "user_message is required"}, status=400)

            # Build the API request
            api_request_json = {
                "messages": [
                    {"role": "user", "content": user_input},
                ],
                
                "stream": False
            }

            # Execute the request to llama
            response = llama.run(api_request_json)

            # Check if response is valid and contains JSON
            if response.status_code == 200:
                try:
                    response_json = response.json()
                except json.JSONDecodeError:
                    return Response({"error": "Invalid JSON response"}, status=500)

                # Extract the assistant's message from the response
                assistant_message = response_json.get('choices', [{}])[0].get('message', {}).get('content', '')

                if assistant_message:
                    # Print the response for debugging (optional)
                    print(json.dumps(response_json, indent=2))

                    # Return the assistant's message to the client
                    return Response({"answer": assistant_message})
                else:
                    return Response({"error": "Assistant message is missing in the response"}, status=500)
            else:
                # Log the error response for debugging
                print(f"API request failed with status {response.status_code} and response: {response.text}")
                return Response({"error": f"API request failed with status {response.status_code}"}, status=response.status_code)

        except Exception as e:
            # Log the exception (optional)
            print(f"Error: {e}")

            # Return an error response
            return JsonResponse({"error": str(e)}, status=500)

import requests
from decouple import config

def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/power-greg/super-fast-llm"
    headers = {"Authorization": f"Bearer {config('HUGGING_FACE_API_KEY')}"}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

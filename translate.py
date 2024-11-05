import requests
import uuid
import json
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('TRANSLATE_KEY')
endpoint = os.getenv('TRANSLATE_API')
location = os.getenv('TRANSLATE_REGION')

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'fr',
    'to': ['en', 'zu']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text': 'J’aimerais vraiment conduire votre voiture autour du pâté de maisons plusieurs fois !'
}]

response = requests.post(constructed_url, params=params, headers=headers, json=body)

if response.status_code == 200:
    response_json = response.json()
    print(json.dumps(response_json, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
else:
    print(f"Error: {response.status_code}")
    print(response.text)

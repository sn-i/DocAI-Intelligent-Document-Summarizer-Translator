import requests
import uuid
import json
from dotenv import load_dotenv
import os
from txtsummary import TxtSummary

load_dotenv()


class Translate:
    def __init__(self):
        self.key = os.getenv('TRANSLATE_KEY')
        self.endpoint = os.getenv('TRANSLATE_API')
        self.location = os.getenv('TRANSLATE_REGION')

    def translate(self):
        path = '/translate'
        constructed_url = self.endpoint + path

        from_lang = input("From which language you want to translate? ")
        to_lang = input("To which language do you want to translate? ")

        params = {
            'api-version': '3.0',
            'from': from_lang,
            'to': [to_lang]
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        txt_summary = TxtSummary()
        summary_text = txt_summary.sample_extractive_summarization()

        if summary_text is None:
            print("Failed to generate summary.")
            return

        body = [{'text': summary_text}]

        response = requests.post(constructed_url, params=params, headers=headers, json=body)

        if response.status_code == 200:
            response_json = response.json()
            print(json.dumps(response_json, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


translate = Translate()
translate.translate()

#The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document. These sentences collectively convey the main idea of the document. This feature is provided as an API for developers.They can use it to build intelligent solutions based on the relevant information extracted to support various use cases.Extractive summarization supports several languages. It is based on pretrained multilingual transformer models, part of our quest for holistic representations.It draws its strength from transfer learning across monolingual and harness the shared nature of languages to produce models of improved quality and efficiency.
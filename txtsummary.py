from azure.ai.textanalytics import TextAnalyticsClient, ExtractiveSummaryAction
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()


class TxtSummary:
    def __init__(self):
        self.key = os.getenv('LANGUAGE_KEY')
        self.endpoint = os.getenv('LANGUAGE_ENDPOINT')
        self.client = self.authenticate_client()

        if not self.key or not self.endpoint:
            raise ValueError("Azure API key or endpoint not set. Check your environment variables.")

    def authenticate_client(self):
        ta_credential = AzureKeyCredential(self.key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=self.endpoint,
            credential=ta_credential
        )
        return text_analytics_client

    def sample_extractive_summarization(self):
        document = input("Enter text to summarize: ")

        poller = self.client.begin_analyze_actions(
            [document],  # document must be a list of strings
            actions=[
                ExtractiveSummaryAction(max_sentence_count=4)
            ],
        )

        document_results = poller.result()
        for result in document_results:
            extract_summary_result = result[0]  # First document, first result
            if extract_summary_result.is_error:
                print(f"Error with code '{extract_summary_result.code}' and message '{extract_summary_result.message}'")
            else:
                # Display summary
                summary = " ".join([sentence.text for sentence in extract_summary_result.sentences])
                print("Summary extracted: \n", summary)


txt = TxtSummary()
txt.sample_extractive_summarization()

#The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document. These sentences collectively convey the main idea of the document. This feature is provided as an API for developers.They can use it to build intelligent solutions based on the relevant information extracted to support various use cases.Extractive summarization supports several languages. It is based on pretrained multilingual transformer models, part of our quest for holistic representations.It draws its strength from transfer learning across monolingual and harness the shared nature of languages to produce models of improved quality and efficiency.

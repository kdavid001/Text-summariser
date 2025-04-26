from flask import Flask, request, jsonify, render_template
import time
import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()
key = os.getenv('AZURE_AI_KEY')
endpoint = os.getenv("ENDPOINT_TO_CALL_LANGUAGE_API")

app = Flask(__name__)


#Autheticate_User
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=ta_credential)
    return text_analytics_client



# Error message
def show_error(message):
    return jsonify({'error': message}), 400



def sample_extractive_summarization(client, input_text):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    )

    document = [input_text]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            return ("Summary extracted:{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )


@app.route('/')
def index():
    return render_template('Home.html')


@app.route('/summarize', methods=['POST'])
def summarize_text():
    client = authenticate_client()
    data = request.get_json()

    if not data or 'text' not in data:
        return show_error('Please provide text to summarize.')

    input_text = data['text'].strip()

    if not input_text:
        return show_error('Please enter some text to summarize.')

    try:
        summary = sample_extractive_summarization(client, input_text)
        return jsonify({'summary': summary})
    except Exception:
        return show_error('An error occurred while summarizing. Please try again.')


if __name__ == "__main__":
    app.run(debug=True)

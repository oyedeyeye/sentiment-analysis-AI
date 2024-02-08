"""
sentiment_analyzer: leverage IBM Watson AI library to conduct sentiment analysis on input text
"""
import json
import requests

# text_to_analyse = "I love this new technology."

def sentiment_analyzer(text_to_analyse):
    """Returns analysis of sentiment in input text

    Arguments:
        text_to_analyse: string dict that is to be analyzed
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/\
            v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    response = requests.post(url, json = myobj, headers=header, timeout=60)
    # Convert response text to json/dict
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    elif response.status_code == 500:
        label = None
        score = None

    return {
        'label': label,
        'score': score
    }

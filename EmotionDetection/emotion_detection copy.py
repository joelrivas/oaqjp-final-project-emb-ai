"""Emotion Detection Module"""
import json
import requests

def emotion_detector(text_to_analyze):
    """Detects the emotion of the given text using an external API."""
    url='https://sn-watson-emotion.labs.skills.network/v1/'+\
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    formated_response = json.loads(requests.post(url, headers=headers, json=input_json).text)

    dominant_emotion = None
    dominant_emotion_score = 0.0
    emotions = {}

    for emotion, score in formated_response['emotionPredictions'][0]['emotion'].items():
        emotions[emotion] = score
        if score > dominant_emotion_score:
            dominant_emotion = emotion
            dominant_emotion_score = score
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
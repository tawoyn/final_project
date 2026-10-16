"""
Emotion Detection Module using IBM Watson NLP Library.
"""

import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the input text using Watson NLP Emotion Detection API.
    Returns a dictionary of emotion scores and the dominant emotion.
    Handles blank inputs by returning None values when status_code is 400.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated_workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
        
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return output

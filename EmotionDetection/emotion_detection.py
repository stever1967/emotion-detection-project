import requests 
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    status_code = response.status_code 
    if status_code == 400 or status_code == 500: 
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return output

    formatted_response = json.loads(response.text)

    emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    emotion_scores = {}
    for emotion in emotions:
        emotion_scores[emotion] = formatted_response["emotionPredictions"][0]["emotion"][emotion]

    dominant_emotion_score = max(emotion_scores.values())
    for emotion, score in emotion_scores.items():
        if score == dominant_emotion_score:
            dominant_emotion = emotion

    output = {
        'anger': emotion_scores["anger"],
        'disgust': emotion_scores["disgust"],
        'fear': emotion_scores["fear"],
        'joy': emotion_scores["joy"],
        'sadness': emotion_scores["sadness"],
        'dominant_emotion': dominant_emotion
    }
    return output


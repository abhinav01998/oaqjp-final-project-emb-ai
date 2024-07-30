import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers = headers, json = json_input)
    json_response = json.loads(response.text)

    if response.status_code == 400:
        return { 'anger': None,
             'disgust': None,
             'fear': None,
             'joy': None,
             'sadness': None,
             'dominant_emotion': None
            }

    anger_score = json_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = json_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = json_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = json_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = json_response['emotionPredictions'][0]['emotion']['sadness']

    highest_emotion_score = max(anger_score, joy_score, fear_score, disgust_score, sadness_score)

    dominant_emotion = list(json_response['emotionPredictions'][0]['emotion'].keys())[list(json_response['emotionPredictions'][0]['emotion'].values()).index(highest_emotion_score)]

    return { 'anger': anger_score,
             'disgust': disgust_score,
             'fear': fear_score,
             'joy': joy_score,
             'sadness': sadness_score,
             'dominant_emotion': dominant_emotion
            }
import requests

def emotion_detector(text_to_analyse):
    """
    Detects the emotion of the given text.
    Parameters:
    text_to_analyse (str): The text to analyze.
    Returns:
    str: A string containing the detected emotions and scores.
    """
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json= { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=json)

    if response.status_code == 400:
        formatted_result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:

        formatted_data = response.json()

        emotions = formatted_data['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotions, key = emotions.get)

        formatted_result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    return formatted_result


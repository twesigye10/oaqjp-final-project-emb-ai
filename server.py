"""
Server that runs the application
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Server")

@app.route('/emotionDetector')
def detect_emotion():
    """
    Endpoint to detect emotion from text. Returns formatted result.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return jsonify({'error': 'No text provided'}), 400

    result = emotion_detector(text_to_analyse)
    if result['dominant_emotion'] is None:
        formatted_result = "Invalid text! Please try again!"
    else:
        formatted_result = f"""
        For the given statement, the system response is 'anger': 0.{result['anger']},
        'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and
        'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.
        """
    return formatted_result

@app.route('/')
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

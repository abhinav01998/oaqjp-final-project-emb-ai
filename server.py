''' This program calls the required functionalities and deploys the flask application ''' 

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotions():
    ''' This function receives the input text for which we detect
        different emotions and also the value of dominant emotion '''
    input_text = request.args.get('textToAnalyze')
    response = emotion_detector(input_text)

    # In case of no text being received
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {response['anger']},
            'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},
            'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}
            ."""

@app.route("/")
def render_index_page():
    ''' This function is used to render the html index/home page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

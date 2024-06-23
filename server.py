"""Module to run the server."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """Calls API and formats output."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    output = f'''For the given statement, the system response is
     'anger': {response["anger"]}, 'disgust': {response["disgust"]},
     'fear': {response["fear"]}, 'joy': {response["joy"]} and
     'sadness': {response["sadness"]}. The dominant emotion is {response["dominant_emotion"]}.'''
    return output

@app.route("/")
def render_index_page():
    """Renders index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

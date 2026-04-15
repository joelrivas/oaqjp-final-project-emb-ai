"""Emotion Detection server"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """Emotion detection."""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    system_response = f"""
For the given statement, the system response is 
'anger': {emotions['anger']}, 
'disgust': {emotions['disgust']}, 
'fear': {emotions['fear']}, 
'joy': {emotions['joy']} and 
'sadness': {emotions['sadness']}. 

The dominant emotion is {emotions['dominant_emotion']}.
"""
    return system_response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

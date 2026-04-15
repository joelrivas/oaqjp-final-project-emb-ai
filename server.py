"""Emotion Detection server"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Emotion detection."""
    if request.method == "POST":
        text_to_analyze = request.form['textToAnalyze']
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
        return render_template('index.html', system_response=system_response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

"""
server.py - A simple Flask web application for detecting emotions in user input
using the Watson NLP Emotion Prediction API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Detection_App")

@app.route('/')
def render_homepage() -> str:
    """
    Renders the home page template.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_analysis() -> str:
    """
    Performs emotion analysis on the provided text and returns a formatted response.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    analysis_result = emotion_detector(text_to_analyze)

    if not text_to_analyze or analysis_result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    response = "For the given statement, the system response is: "

    emotion_parts = [
        f"'{emotion}': {score:.6f}"
        for emotion, score in analysis_result.items()
        if emotion != "dominant_emotion"
    ]

    response += ", ".join(emotion_parts)
    response += f". The dominant emotion is {analysis_result['dominant_emotion']}."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    body = request.get_json()
    inputText = body.get("comment", "")
    
    if not inputText:
        return jsonify({"error": "Comment Not Provided"}), 400

    blob = TextBlob(inputText)
    score = blob.sentiment.polarity

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    response = {
        "sentiment": sentiment,
        "confidence": abs(score)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

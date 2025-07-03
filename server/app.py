from flask import Flask, request, jsonify
from flask_cors import CORS
from ml.emotion_detector import detect_emotion
from ml.ai_response import generate_response
from db.chat_model import save_chat

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("user_input") or data.get("message")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Detect emotion
    emotion = detect_emotion(user_input)

    # Generate dynamic AI response
    ai_response = generate_response(user_input)

    # Save chat to DB
    save_chat(user_input, ai_response, emotion)

    return jsonify({
        "ai_response": ai_response,
        "emotion": emotion
    })

if __name__ == "__main__":
    app.run(debug=True)

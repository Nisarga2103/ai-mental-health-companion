# routes/chat_routes.py

from flask import Blueprint, request, jsonify
from ml.emotion_detector import detect_emotion
from ml.ai_response import generate_response
from db.chat_model import save_chat, get_all_chats

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    emotion = detect_emotion(user_input)
    ai_response = generate_response(user_input, emotion)  # <-- updated to pass emotion

    save_chat(user_input, ai_response, emotion)

    return jsonify({
        "response": ai_response,
        "emotion": emotion
    })

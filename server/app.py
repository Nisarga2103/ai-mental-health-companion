from flask import Flask, request, jsonify
from flask_cors import CORS
from db.chat_model import save_chat  # Function to save chats into the DB
from ml.emotion_detector import detect_emotion  # Emotion detection logic
from ml.ai_response import generate_response  # AI response generator

app = Flask(__name__)
CORS(app)  # Enable CORS for communication with the React frontend

# Route for handling user input and generating AI response
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("user_input")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Detect emotion from the user input
        emotion = detect_emotion(user_input)

        # ✅ FIXED: Pass both user_input and emotion to generate_response
        ai_response = generate_response(user_input, emotion)

        # Save chat to the database
        save_chat(user_input, ai_response, emotion)

        # Return AI response and detected emotion
        return jsonify({
            "ai_response": ai_response,
            "emotion": emotion
        })

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

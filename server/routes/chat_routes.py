import datetime

def save_chat(user_input, ai_response, emotion):
    # For demonstration, just log to a text file
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | User: {user_input} | AI: {ai_response} | Emotion: {emotion}\n")

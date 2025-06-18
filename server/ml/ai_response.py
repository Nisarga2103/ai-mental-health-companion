def generate_response(emotion):
    # Define possible responses based on emotions
    responses = {
        'sad': "I'm sorry you're feeling sad. Want to talk about it?",
        'happy': "That's great to hear! 😊 What made your day better?",
        'angry': "It's okay to feel angry. Let’s take a deep breath together.",
        'anxious': "Anxiety can be overwhelming. I'm here with you. Try focusing on your breathing.",
        'neutral': "I'm here to support you. How are you feeling today?"
    }

    # Normalize the emotion to lowercase for consistency
    emotion = emotion.lower()

    # Return the appropriate response or the default 'neutral' if emotion not found
    return responses.get(emotion, responses['neutral'])

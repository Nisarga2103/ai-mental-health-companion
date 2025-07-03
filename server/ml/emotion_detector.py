def detect_emotion(user_input):
    input_lower = user_input.lower()

    emotion_keywords = {
        'sad': ['sad', 'depressed', 'down', 'blue', 'unhappy'],
        'happy': ['happy', 'joy', 'glad', 'excited', 'cheerful'],
        'angry': ['angry', 'mad', 'furious', 'irritated', 'enraged'],
        'anxious': ['anxious', 'worried', 'nervous', 'uneasy', 'stressed'],
        'neutral': ['fine', 'okay', 'neutral', 'alright', 'good']
    }

    for emotion, keywords in emotion_keywords.items():
        if any(word in input_lower for word in keywords):
            return emotion

    return 'neutral'

from .connection import get_connection

def create_chat_table():
    """Create the chat table if it does not exist"""
    try:
        conn = get_connection()  # Corrected indentation
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_input TEXT,
                ai_response TEXT,
                emotion VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
    except Exception as e:
        print(f"Error creating chat table: {e}")
    finally:
        cursor.close()
        conn.close()

def save_chat(user_input, ai_response, emotion):
    """Save the chat data (user_input, ai_response, emotion) into the chat table"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO chat (user_input, ai_response, emotion) VALUES (%s, %s, %s)",
            (user_input, ai_response, emotion)
        )
        conn.commit()
    except Exception as e:
        print(f"Error saving chat: {e}")
    finally:
        cursor.close()
        conn.close()

def get_all_chats():
    """Fetch all chats from the chat table"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM chat")
        chats = cursor.fetchall()

        return chats
    except Exception as e:
        print(f"Error fetching all chats: {e}")
        return []  # Return an empty list in case of error
    finally:
        cursor.close()
        conn.close()

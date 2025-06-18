import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        
        if connection.is_connected():
            print("Successfully connected to the database.")
        return connection
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

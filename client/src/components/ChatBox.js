// src/components/ChatBox.js
import React, { useState } from "react";
import axios from "axios";
import "./ChatBox.css";

const ChatBox = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userInput.trim()) return;

    // Add user message to chat
    setMessages((prev) => [...prev, { sender: "You", text: userInput }]);

    try {
      const response = await axios.post("http://localhost:5000/chat", {
        user_input: userInput,
      });

      const { ai_response, emotion } = response.data;

      // Add AI response to chat
      setMessages((prev) => [
        ...prev,
        { sender: "AI", text: ai_response, emotion },
      ]);

      setUserInput("");
    } catch (error) {
      console.error("Error:", error);
      setMessages((prev) => [
        ...prev,
        { sender: "AI", text: "Sorry, I couldn't process that." },
      ]);
    }
  };

  return (
    <div className="chatbox-wrapper">
      <div className="chatbox-container">
        <div className="chatbox-title">AI Mental Health Companion</div>
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender === "You" ? "user" : "ai"}`}
            >
              <strong>{msg.sender}:</strong> {msg.text}
              {msg.emotion && (
                <span className="emotion">({msg.emotion})</span>
              )}
            </div>
          ))}
        </div>
        <form className="chat-input" onSubmit={handleSubmit}>
          <input
            type="text"
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            placeholder="Type your message..."
          />
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
};

export default ChatBox;

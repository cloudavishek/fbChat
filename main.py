from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Load the DeepSeek API key from environment variables
DEEPSEEK_API_KEY = os.getenv("sk-adb3291e9fe84992b6c49c85093b2e52")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/webhook", methods=["POST"])
def webhook():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    headers = {
        "Authorization": f"Bearer {sk-adb3291e9fe84992b6c49c85093b2e52}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        reply = response.json().get("choices")[0].get("message").get("content")
        return jsonify({"reply": reply})
    else:
        return jsonify({"error": "Failed to get response from DeepSeek"}), 500

@app.route("/")
def home():
    return "DeepSeek AI Chatbot is running!"

if __name__ == "__main__":
    app.run(debug=True)

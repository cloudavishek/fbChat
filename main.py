from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Add your OpenAI key in Railway secrets

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_msg = data.get('message', '')

    # Call OpenAI API
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_msg}],
            "max_tokens": 150
        }
    ).json()

    bot_reply = response['choices'][0]['message']['content']
    return jsonify({"reply": bot_reply})

@app.route('/')
def home():
    return "Chatbot is running!"

if __name__ == '__main__':
    app.run(debug=True)

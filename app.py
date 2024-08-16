from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import os

# Retrieve your OpenAI API key and base URL from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE_URL", "https://api.pawan.krd/pai-001-light-beta/v1")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Chatbot API. Use /api/route to interact with the chatbot."

@app.route('/api/route', methods=['POST', 'GET'])
def chatbot():
    data = request.get_json()
    user_input = data.get('text', "")

    if not user_input:
        return jsonify({'response': 'No input provided'}), 400

    response = openai.ChatCompletion.create(
        model="pai-001-light-beta",
        messages=[
            {'role': 'user', 'content': user_input},
        ],
        stream=True,
        allow_fallback=True
    )

    content_string = ""
    for chunk in response:
        content_string += chunk.choices[0].delta.get("content", "")

    response_text = content_string
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

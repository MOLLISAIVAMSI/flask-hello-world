from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for the Flask app
CORS(app)

@app.route('/')
def hello_world():
    response_text = "Hello, World!"
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)

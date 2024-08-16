from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    response_text = "Hello, World!"
    return jsonify({'response': response_text})

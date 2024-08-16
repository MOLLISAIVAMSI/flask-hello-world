from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    response_text = "Hello, World!"
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)

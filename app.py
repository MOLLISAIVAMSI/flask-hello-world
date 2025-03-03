from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

SERVICES = {
    "app1": "http://localhost:5001",
    "app2": "http://localhost:5002",
    "app3": "http://localhost:5003"
}

@app.route('/')
def home():
    return jsonify({"message": "Flask Gateway Running!"})

@app.route('/api/<service>', methods=['GET', 'POST'])
def proxy(service):
    if service not in SERVICES:
        return jsonify({"error": "Service not found"}), 404
    
    target_url = SERVICES[service] + request.path
    if request.method == "POST":
        response = requests.post(target_url, json=request.json)
    else:
        response = requests.get(target_url)
    
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Gateway runs on port 10000

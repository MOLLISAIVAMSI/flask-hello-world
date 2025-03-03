# gateway.py
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

@app.route('/api/<service>/<path:subpath>', methods=['GET', 'POST'])
def proxy(service, subpath):
    if service not in SERVICES:
        return jsonify({"error": "Service not found"}), 404
    
    target_url = f"{SERVICES[service]}/{subpath}"
    
    try:
        if request.method == "POST":
            response = requests.post(target_url, json=request.json)
        else:
            response = requests.get(target_url)
        
        return response.json()
    except requests.exceptions.ConnectionError:
        return jsonify({"error": f"Could not connect to {service}"}), 503

@app.route('/api/<service>', methods=['GET', 'POST'])
def proxy_root(service):
    if service not in SERVICES:
        return jsonify({"error": "Service not found"}), 404
    
    target_url = SERVICES[service]
    
    try:
        if request.method == "POST":
            response = requests.post(target_url, json=request.json)
        else:
            response = requests.get(target_url)
        
        return response.json()
    except requests.exceptions.ConnectionError:
        return jsonify({"error": f"Could not connect to {service}"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Gateway runs on port 10000

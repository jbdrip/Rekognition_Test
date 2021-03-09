from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send
from flask_cors import CORS
import json
import boto3
import base64


app = Flask(__name__)
CORS(app)
socket = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods = ['GET'])
def init():
    return "Server working correctly."

@app.route('/tarea3-201730555', methods=['POST'])
def image():
    client = boto3.client(
        'rekognition',
        region_name             = '',
        aws_access_key_id       = '',
        aws_secret_access_key   = ''
    )
    data = request.get_json()
    response = client.detect_labels(
        Image = { 'Bytes': base64.b64decode(data["base64"])}
    )
    return jsonify(response)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
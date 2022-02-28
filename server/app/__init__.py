from flask import Flask, request, redirect
from flask_cors import cross_origin
from . import creation_model
import json

app = Flask(__name__)
app.config['TESTING'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.testing = True
HOST = "127.0.0.1"
PORT = 5000


@app.route('/')
def index():
    return ""


@app.route('/model', methods=['POST'])
@cross_origin(origin='127.0.0.1', headers=['Content- Type', 'Authorization'])
def model():
    print("Enter a sentence to analyse :")
    sentence = request.json['sentence']
    result = creation_model.sentiment_scores(sentence)
    json_result = json.dumps(result)
    return json_result, 200


if __name__ == "__main__":
    app.run(HOST, PORT, debug=True)


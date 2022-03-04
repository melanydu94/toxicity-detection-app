from flask import Flask, request, redirect, Response
from flask_cors import CORS, cross_origin
from . import creation_model
import json
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time



app = Flask(__name__)
CORS(app)
app.config['TESTING'] = True
app.testing = True
HOST = "127.0.0.1"
PORT = 5000

_INF = float('inf')

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds', buckets={1, 2, 5, 6, 10, _INF})

@app.route('/')
def index():
    return ""


@app.route('/model', methods=['POST'])
def model():
    start = time.time()
    graphs['c'].inc()

    print("Enter a sentence to analyse :")

    sentence = request.json['sentence']
    result = creation_model.sentiment_scores([sentence])
    json_result = json.dumps(result)
    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return json_result, 200

@app.route('/metrics', methods=['GET'])
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

if __name__ == "__main__":
    app.run(HOST, debug=True)


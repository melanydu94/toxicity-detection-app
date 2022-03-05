from server.app import app
import json
import os.path
from os import path
import requests

app.testing = True

# cmd to un test : python -m pytest test/test_model.py

def test_site_working_well(client):
    response = client.post('/model', json={"sentence": "I'm happy"})
    assert response.status_code == 200
    
def test_threat(client):
    response = client.post('/model', json={"sentence": "I will kill you"})
    data = json.loads(response.data)
    assert data["threat"] > 0.5
    
def test_check_response_format(client):
    response = client.post('/model', json={"sentence": "I don't like it"})
    assert response.headers.get('content-type') == 'text/html; charset=utf-8'
    
def test_check_presence_model():
    model = path.exists("server/app/toxic_original-c1212f89.ckpt")
    assert model == True

"""
def test_handle_100_requests_per_minute(client):
    requests_url = ['http://127.0.0.1:5000/model?sentence="I do not like it"'] * 100
    list_elapsed_time = []
    val_elapsed_time = 0
    for url in requests_url:
        response = requests.get(url)
        list_elapsed_time.append(response.elapsed)
        val_elapsed_time = val_elapsed_time + response.elapsed.total_seconds()

    avg_elapsed_time = val_elapsed_time / len(list_elapsed_time)
    print(avg_elapsed_time)  # time in seconds
    assert avg_elapsed_time < 0.1  # 100 ms
"""    

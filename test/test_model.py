from server.app import app
import json


app.testing = True

"""
def test_check_response(client):
    response = client.get('/model')
    data = json.loads(response.data)
    assert data == 3.0
"""


def test_site_working_well(client):
    response = client.post('/model', json={"sentence": "i'm happy"})
    assert response.status_code == 200
    
def test_positive(client):
    response = client.post('/model', json={"sentence": "i'm happy"})
    data = json.loads(response.data)
    assert data["Sentiment"] == "Positive"
    
def test_negative(client):
    response = client.post('/model', json={"sentence": "i'm sad"})
    data = json.loads(response.data)
    assert data["Sentiment"] == "Negative"
    
def test_neutral(client):
    response = client.post('/model', json={"sentence": "i'm a fireman"})
    data = json.loads(response.data)
    assert data["Sentiment"] == "Neutral"
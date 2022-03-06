import pytest
from server.app import app


@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    return client

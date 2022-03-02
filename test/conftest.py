import pytest
from server.model import app


@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    return client

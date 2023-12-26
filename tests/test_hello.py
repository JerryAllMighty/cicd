import pytest
from hello import app

@pytest.fixture()
def client():
    return app.test_client()

def test_hello_world(client):
    res = client.get('/')
    assert res.status_code == 200
    
def test_index(client):
    res = client.get('/index')
    assert res.status_code == 200
    
    

    
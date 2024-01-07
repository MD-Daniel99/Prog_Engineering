# test_app.py
from assignment_2 import model_loading, get_url
from fastapi.testclient import TestClient
from assignment_2 import app

client = TestClient(app)

def test_model_loading():
    model = model_loading()
    assert model is not None  

def test_get_url():
    assert get_url("https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp") 



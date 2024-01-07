# test_app.py
from main.assignment_2 import model_loading, get_url

def test_model_loading():
    model = model_loading()
    assert model is not None  

def test_get_url():
    assert is_valid_image_url("https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp") 



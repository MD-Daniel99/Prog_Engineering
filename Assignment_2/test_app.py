import requests
import pytest
from main import model_loading, get_url, processing, printing

BASE_URL = "https://astronaut-snowboarding-across-theuniverse.streamlit.app"

# Тесты
def test_root_endpoint():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_http_status_code():
    data = {"image_url": "example.jpg"}
    response = requests.post(f"{BASE_URL}/process_image", json=data)
    assert response.status_code == 200

def test_response_content():
    data = {"image_url": "example.jpg"}
    response = requests.post(f"{BASE_URL}/process_image", json=data)
    assert "description" in response.json()

def test_valid_image_url():
    # Мы не можем тестировать функцию get_url напрямую, так как она взаимодействует с вводом пользователя
    # Вместо этого мы проверяем, что получаемый URL валиден
    assert get_url() is not None

def test_app_availability():
    response = requests.get(f"{BASE_URL}/process_image")
    assert response.status_code == 200

def test_model_loading():
    assert model_loading() is not None

def test_image_recognition_result():
    data = {"image_url": "https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp"}
    response = requests.post(f"{BASE_URL}/process_image", json=data)
    assert "Image described:" in response.text

import requests
import json

BASE_URL = "https://astronaut-snowboarding-across-theuniverse.streamlit.app"

def test_response_content():
    data = {"image_url": "example.jpg"}
    response = requests.post(f"{BASE_URL}/process_image", json=data)
    
    # Проверяем, что ответ содержит JSON-данные
    assert "description" in response.json()

# Удаляем тест, так как теперь у вас фиксированный URL
# def test_valid_image_url():
#     assert get_url() is not None

def test_image_recognition_result():
    data = {"image_url": "https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp"}
    response = requests.post(f"{BASE_URL}/process_image", json=data)
    
    # Проверяем, что "Image described:" есть в тексте ответа
    assert "Image described:" in response.text

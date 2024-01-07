# test_app.py
from main.assignment_2 import model_loading, is_valid_image_url

def test_model_loading():
    model = model_loading()
    assert model is not None  # Проверьте, что модель успешно загружена

def test_is_valid_image_url():
    assert is_valid_image_url("https://example.com/image.jpg")  # Подставьте реальные тестовые URL

# Добавьте другие тесты для ваших функций, если это возможно

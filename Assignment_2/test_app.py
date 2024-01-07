import pytest
from unittest.mock import patch
from main import model_loading, get_url, processing, printing

# Тест 1: Проверка, что модель загружена
def test_model_loading():
    classifier = model_loading()
    assert classifier is not None

# Тест 2: Проверка, что url-картинки получено
@patch("streamlit.text_input", return_value="https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp")
def test_get_url(mock_text_input):
    get_image_url = get_url()
    assert get_image_url == "https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp"

# Тест 3: Проверка вывода результата работы модели
@patch("streamlit.button", return_value=True)
def test_processing_and_printing(mock_button):
    pred = model_loading()
    get_image_url = "https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp"
    res = pred(get_image_url)
    assert res is not None

# Запуск тестов
if __name__ == "__main__":
    pytest.main(["-v", "--capture=no", "test_app.py"])

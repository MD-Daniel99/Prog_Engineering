import pytest
import streamlit as st
from unittest.mock import patch
from assignment_2  import model_loading, get_url, processing, printing

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
@patch("main.model_loading")
@patch("main.printing")
def test_processing(mock_printing, mock_model_loading, mock_button):
    pred_mock = mock_model_loading.return_value
    res = "mocked result"
    
    # Подмена результата работы модели
    pred_mock.return_value = res
    
    # Запуск теста
    processing("https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp", pred_mock)
    
    # Проверка, что модель была вызвана с корректными аргументами
    pred_mock.assert_called_once_with("https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp")
    
    # Проверка, что результат был передан в функцию печати
    mock_printing.assert_called_once_with(res)

# Запуск тестов
if __name__ == "__main__":
    pytest.assignment_2(["-v", "--capture=no", "test_app.py"])

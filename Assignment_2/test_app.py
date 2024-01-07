import pytest
import streamlit as st
from main import model_loading, get_url, processing, printing

# Тест 1: Проверка, что модель загружена
def test_model_loading():
    classifier = model_loading()
    assert classifier is not None

# Тест 2: Проверка, что url-картинки получено
def test_get_url():
    with st.button("Click to start"):
        st.text_input("Enter picture URL:", value="https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp")
    get_image_url = get_url()
    assert get_image_url == "https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp"

# Тест 3: Проверка вывода результата работы модели
def test_processing_and_printing():
    with st.button("Click to start"):
        st.text_input("Enter picture URL:", value="https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp")
    pred = model_loading()
    get_image_url = get_url()
    res = None
    with st.button("Click to start"):
        res = pred(get_image_url)
    with st.button("Click to start"):
        printing(res)
    assert st.get_last_widget_value() == "Image described:\n" + res

# Запуск тестов
if __name__ == "__main__":
    pytest.main(["-v", "--capture=no", "test_app.py"])

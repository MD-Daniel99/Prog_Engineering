# test_app.py
import streamlit_e2e_testing as st
from assignment_2 import model_loading, get_url, processing, printing

# 1. Первый тест проверяет доступность приложения при обращении к корню сервера
def test_root_endpoint():
    st._init()
    with st._exception_handler():
        st.script_run("assignment_2.py")  # Подставьте правильный путь к вашему приложению
    st.expect("Image-to-text model")

# 2. Тест проверяет код ответа HTTP
def test_http_status_code():
    st._init()
    with st._exception_handler():
        st.script_run("assignment_2.py")  # Подставьте правильный путь к вашему приложению
    st.submit_form({"Enter picture URL:": "example.jpg", "Click to start": None})
    st.expect_code(200)

# 3. Тест проверяет содержание ответа
def test_response_content():
    st._init()
    with st._exception_handler():
        st.script_run("assignment_2.py")  # Подставьте правильный путь к вашему приложению
    st.submit_form({"Enter picture URL:": "example.jpg", "Click to start": None})
    st.expect("Image described:")

# 4. Тест проверяет, что программе предоставлена URL-ссылка на картинку
def test_valid_image_url():
    assert get_url() is not None

# 5. Тест проверяет доступность приложения. Код статуса ответа HTTP должен быть равен 200
def test_app_availability():
    st._init()
    with st._exception_handler():
        st.script_run("assignment_2.py")  # Подставьте правильный путь к вашему приложению
    st.expect_code(200)

# 6. Тест проверяет, что модель успешно загружена
def test_model_loading():
    assert model_loading() is not None

# 7. Тест проверяет результат распознавания картинки и выводит текстовое описание картинки
def test_image_recognition_result():
    st._init()
    with st._exception_handler():
        st.script_run("assignment_2.py")  # Подставьте правильный путь к вашему приложению
    st.submit_form({"Enter picture URL:": "https://www.quickanddirtytips.com/wp-content/uploads/2019/12/astronaut-jpg.webp", "Click to start": None})
    st.expect("Image described:")
 



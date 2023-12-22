from transformers import pipeline
from transformers import AutoTokenizer
import torch
import tensorflow
from docx import Document
from pdfminer.high_level import extract_text
import streamlit as st
import io

st.page_title("Brevity is the soul of wit...")

# Функиця get_data() предоставляет пользователю выбор: загрузить для обработки файл одного из предложенных форматов, либо ввести текст в предложенное поле
def get_data():
  # Обновляет поле ввода текста или загрузки файла после окончания работы программы
  st.session_state.translation_choice = None
  source_button = st.radio(
      "\nВыберите источник данных",
      ["Загрузка файла", "Ввод текста"],
      captions=["Загрузить текст из файла", "Вставить текст из буфера или ввести с клавиатуры"]
  )
  # Если выбран ввод с клавиатуры - возвращается str, содержащая ввеженный текст
  if source_button == "Ввод текста":
      text = st.text_area("Введите текст")
      if text is not None:
        text_button = st.button('Обработать текст')
        if text_button:
          return text.rstrip()
      else:
        return
      
  # Если выбрана загрузка файла - начинается процесс анализа формата файла.
      # В зависимости от формата используются разные модули для декодирования текста 
  elif source_button == "Загрузка файла":
      uploaded_file = st.file_uploader("Выберите файл", type=["txt", "docx", "pdf"], accept_multiple_files=False)
      if uploaded_file is not None:
        file_content = uploaded_file.read()

    # Проверка, имеет ли файл расширение .docx
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
          st.text("Word Document Detected")

              # Обернуть содержимое файла в объект BytesIO
          file = io.BytesIO(file_content)
          doc = Document(file)
          text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

    # Проверка, имеет ли файл расширение .pdf
        elif uploaded_file.type == "application/pdf":
          st.text("PDF Document Detected")

              # Точно также, обернуть содержимое файла в объект BytesIO
          file = io.BytesIO(file_content)
          text = extract_text(file)

    # Если не .docx и не .pdf, значит - .txt
          # Это черновое решение: Streamlit создает кучу сложностей принципом своей работы, что заставляет изворачиваться
        else:
          st.text("TXT Document Detected")
          with open(file_content, 'r') as file_object:
            text = file_object.read()

    # Возвращем text, полученный одним из вышеуказанных методов (в зависимости от выбранной пользователем опции)
        button = st.button('Обработать файл')
        if button:
          return text.rstrip() 
      else:
        return

def trim_text_to_token_limit(content, max_token_limit=512, model_name="Falconsai/text_summarization"):
  # Загрузка токенизатора для заданной модели
  tokenizer = AutoTokenizer.from_pretrained(model_name)

  # Преобразование content в строку (если это не строка)
  content_str = str(content)

  # Токенизация текста
  tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(content_str)))

  # Обрезка текста до заданного количества токенов
  trimmed_tokens = tokens[:max_token_limit]

  # Обратная токенизация для получения текста
  trimmed_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(trimmed_tokens))

  return trimmed_text

def summary_model(contents, trimmed_text):
  #contents = pipeline('summarization', model = "Falconsai/text_summarization")
  summarised_text = contents(trimmed_text, min_length = 70)[0]
  summary = summarised_text['summary_text'] # тип данных = строка
  print(type(summary), "\n", summary)
  return summary

@st.cache_resource
def tr_model_loading():
  translator = pipeline("translation_en_to_ru", model = "Helsinki-NLP/opus-mt-en-ru")
  return translator

@st.cache_resource
def sum_model_loading():
  summariser = pipeline('summarization', model = "Falconsai/text_summarization")
  return summariser

def translation(classifier, summary):
  translation_radio_button = st.radio(
      "\nВыберите опцию перевода",
      ["Перевести текст", "Не переводить"],
      key="translation", index = None
  )
  if translation_radio_button == "Перевести текст":
      sentences = summary.split('. ')
      translated_sentences = [classifier(sentence)[0]['translation_text'] for sentence in sentences]
      translated_summary = '. '.join(translated_sentences)
      return translated_summary
  
  elif translation_radio_button == "Не переводить":
      return summary


def writing_into_file(translated):
  if translated is not None:
    output_file = 'processed_text.txt'
    with open(output_file, 'w') as file:
      file.write(translated)
    
    st.download_button(
      label="Скачать файл",
      data=open(output_file, "rb").read(),
      file_name=output_file,
      key="download_button",
      )

def main():
  # Предвосхищаем возможность получить None в процессе получения данных - обрабатываем исключение
  try:
    # Загрузка двух моделей машинного обучения с применением Streamlit-кэширования, что позволяет не загружать модели заново при повторном использовании программы
      # translator - модель-переводчик, summariser - модель-стенографист
    translator = tr_model_loading() 
    summariser = sum_model_loading()

    # Вызов функции для загрузки данных - текстового файла или ввода с клавиатуры. Результат, вне зависимости от способа получения данных, 
    # сохраняется в переменной content
    content = get_data() 

    # Модель Falconsai/text_summarization, осуществляющая конспектирование текста, не способна обработать текст, количество токенов в которой превышает 512, 
      # в связи с чем не рекомендуется загружать в модель текст большого объема - начинает вести себя некорректно.
        # функция def trim_text_to_token_limit() динамически усекает
          # количество токенов в предложенном тексте до доступного максимума.
    trimmed_text = trim_text_to_token_limit(content)

    # Укороченный в trimmed_text() текст проходит процесс конспектирования в функции summary_model() с последующим сохранением результата в переменной summary
    summary = summary_model(summariser, trimmed_text) # МОДЕЛЬ номер 1 - резюме

    # По выбору пользователя(внутри функции translation) производится пеервод конспекта с последующим сохранением результата в переменной prediction
    prediction = translation(translator, summary) # МОДЕЛЬ номер 2 - перевод

    # Осуществляется запись обработанного текста в созданный файл.txt с последующей возможность его скачивания
    writing_into_file(prediction)

  # Если в процессе выполнения программы возникает ValueError вследсвие получения None Type - обрабатываем исключение
  except ValueError:
    st.write("Не удалось распознать текст или файл, пожалуйста, повторите попытку")
    return

# Вначале был main()
main() 

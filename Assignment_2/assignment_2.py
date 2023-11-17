import io
from transformers import pipeline
import torch
import streamlit as st

@st.cache_resource
def model_loading():
  classifier = pipeline("image-to-text", model = "nlpconnect/vit-gpt2-image-captioning")
  return classifier

def get_url():
  get_image_url = st.text_input("Enter picture URL:")
  if get_image_url:
    st.image(get_image_url, use_column_width = True)
    return get_image_url

def processing(get_image_url, pred):
  button = st.button("Click to start")
  if button:
    res = pred(get_image_url)
    printing(res)

def printing(res):
  st.write("Image described:")
  st.write(res)

st.title("Image-to-text model")
pred = model_loading()
link = get_url()
processing(link, pred)

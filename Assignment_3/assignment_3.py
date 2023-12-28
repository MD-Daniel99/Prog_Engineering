from fastapi import FastAPI
import tensorflow
from transformers import pipeline
import torch

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ImageRequest(BaseModel):
    image_url: str

@app.on_event("startup")
def model_loading():
    app.classifier = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

@app.post("/process_image")
async def process_image(request: ImageRequest):
    try:
        image_url = request.image_url
        result = app.classifier(image_url)
        return {"description": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


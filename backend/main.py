from fastapi import FastAPI, HTTPException
from openai import OpenAI
#import numpy as np
#import pickle
#import pandas as pd
app = FastAPI()
client = OpenAI(api_key)

image_url = ""
@app.get("/stories")
def index(inputstr:str):
    response = client.images.generate(
            model="dall-e-2",
            prompt = inputstr,
            size="256x256",
            quality = "standard",
            n = 1,
            )
    image_url = response.data[0].url
    return image_url


#prompt
#pickle_in = open("model.pkl","rb")
#classifier = pickle.load(pickle_in)
#
#@app.post("/predict")
#def predict(data:_________):
#    data = data.dict()
#
#

from fastapi import FastAPI
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.optim import Adam
from torch.utils.data import DataLoader
from StoryData import StoryData
import torch
import tqdm 
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from StoryData import StoryData
from torch.optim import Adam
from torch.utils.data import DataLoader
import torch
import tqdm 
from main import train, infer

app = FastAPI()

@app.post("/generate")
async def generate_text(input_text: str):
    output_text = infer(input_text)
    return {"output_text": output_text}



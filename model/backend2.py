from fastapi import FastAPI
from main import infer
app = FastAPI()

@app.post("/generate")
async def generate_text(input_text: str):
    output_text = infer(input_text)
    return {"output_text": output_text}


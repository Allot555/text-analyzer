from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Text Analyzer API is running"}


@app.post("/analyze")
def analyze_text(request: TextRequest):
    text = request.text

    words = text.split()

    return {
        "word_count": len(words),
        "character_count": len(text)
    }
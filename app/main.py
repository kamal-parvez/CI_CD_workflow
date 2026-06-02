from fastapi import FastAPI
from pydantic import BaseModel

from app.text_stats import char_count, top_words, word_count

app = FastAPI(title="Text Stats API", version="1.0.0")


class TextIn(BaseModel):
    text: str
    top_n: int = 3


@app.get("/health")
def health() -> dict[str, str]:
    return {"Status": "OK"}


@app.post("/stats")
def stats(payload: TextIn) -> dict:
    return {
        "words": word_count(payload.text),
        "characters": char_count(payload.text),
        "characters_no_spaces": char_count(payload.text, include_spaces=False),
        "top_words": top_words(payload.text, payload.top_n),
    }

# project to create a motivational quotes adder! just the backend progress on my own...
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Quote(BaseModel):
    quote: str


all_quotes: List[Quote] = []


@app.post("/add_quote")
def add_quotes(line: Quote):
    all_quotes.append(line)
    return {"status": "added new quote", "total_items": len(all_quotes)}


@app.get("/read_quote")
def read_quotes():
    return all_quotes

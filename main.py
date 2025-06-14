from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Load fake DB
with open("fake_db.json", "r") as f:
    database = json.load(f)

class QuestionRequest(BaseModel):
    question: str
    image: str = None  # Optional, not processed

@app.post("/api/")
async def answer_question(q: QuestionRequest):
    question = q.question.lower()

    for item in database:
        if item["question"].lower() in question:
            return {
                "answer": item["answer"],
                "links": item["links"]
            }

    return {
        "answer": "Sorry, I couldn't find an answer to that question.",
        "links": []
    }

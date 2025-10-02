from fastapi import FastAPI
from pydantic import BaseModel
from gpt_client import ask_gpt

app = FastAPI()

# Модель для запиту
class Question(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Сервер працює!"}

@app.post("/ask/")
def ask_question(question: Question):
    answer = ask_gpt(question.prompt, language="uk")
    return {"answer": answer}


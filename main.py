from fastapi import FastAPI
from pydantic import BaseModel

from .rag import search_knowledge_base
from .tools import check_system_status, log_ticket

app = FastAPI()


class UserQuestion(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI IT Helpdesk Agent is running!"
    }


@app.post("/ask")
def ask_helpdesk(data: UserQuestion):

    result = search_knowledge_base(data.question)

    if result:
        return {
            "status": "success",
            "category": result["category"],
            "problem": result["problem"],
            "solution": result["solution"]
        }

    return {
        "status": "not_found",
        "message": "Sorry, I could not find a solution."
    }


@app.get("/system-status")
def system_status():
    return check_system_status()


@app.post("/ticket")
def create_ticket(data: UserQuestion):
    return log_ticket(data.question)
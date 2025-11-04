from fastapi import FastAPI, Query
from .queue import connection

app = FastAPI()

@app.get("/")
def chat():
    return { "status": 'Server is running' }

@app.post("/chat")
def chat(
    query: str = Query(..., description="The user's query"),
):
    pass
from fastapi import FastAPI, Query
from .queue.connection import queue
from .queue.worker import process_query

app = FastAPI()

@app.get("/")
def chat():
    return { "status": 'Server is running' }

@app.post("/chat")
def chat(
    query: str = Query(..., description="The user's query"),
):
    job = queue.enqueue(process_query, query)
    return { "status": "queued", "job_id": job.id }
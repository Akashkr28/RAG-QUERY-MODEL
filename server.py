from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True), override=True)

from fastapi import FastAPI, Query, Path
from .my_queue.connection import queue
from .my_queue.worker import process_query

app = FastAPI()


@app.get("/")
def chat():
    return {"status": 'Server is running'}


@app.post("/chat")
def chat(
    query: str = Query(..., description="The user's query"),
):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}


@app.get("/result/{job_id}")
def get_result(
    job_id: str = Path(..., description="Job ID")
):

    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()
    return {"result": result}

from fastapi import FastAPI,Query,Path
from job_queue.connection import queue
from job_queue.worker import process_query
# from job_queue.tasks import enqueue_query_job
app = FastAPI()


@app.get('/')   
def root():
    return {"status":'Server is up and running'}

@app.post('/chat')
def chat(
    query: str=Query(..., description="Chat Message")
):
    # job = enqueue_query_job(query)
    # return {"status": "queued", "job_id": job.id}
    # return {"status":"queued","job_id":job.id}
    
    # Query ko Queue mei daal do
    job = queue.enqueue(process_query, query)  # process_query(query)

    # User ko bolo your job received
    return {"status": "queued", "job_id": job.id}


@app.get("/result/{job_id}")
def get_result(
    job_id:str=Path(...,description="Job ID")
):
    job=queue.fetch_job(job_id=job_id);
    result=job.return_value();
    return {"result":result}

from job_queue.connection import queue
from job_queue.worker import process_query

def enqueue_query_job(query: str):
    return queue.enqueue(process_query, query)
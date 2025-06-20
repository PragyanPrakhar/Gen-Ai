from redis import Redis
from rq import Queue
# from rq.simple import SimpleWorker

queue = Queue(connection=Redis(host="localhost", port=6379))

# Create a SimpleWorker (no forking — works on Windows)
# worker = SimpleWorker([queue], connection=Redis())

#start the worker
# worker.work(with_scheduler=True)
from celery import Celery

CELERY_BROKER = "redis://localhost"
CELERY_BACKEND = "redis://localhost"
app = Celery("hello", broker=CELERY_BROKER, backend=CELERY_BACKEND)


@app.task
def add(x, y):
    return x + y


@app.task
def fail():
    raise Exception("The task failed")

# tasks.py
from celery import Celery
import time

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    time.sleep(2)
    print("Tarefa em execução!")
    return x + y

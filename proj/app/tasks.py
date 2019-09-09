from celery import shared_task, Celery

@shared_task
def hello():
    print("WORKING ------------------------------------ WORKING !!!")

from celery import shared_task

@shared_task
def send_notification():
    # Logic to send notifications to employees not registered for 2 days
    pass

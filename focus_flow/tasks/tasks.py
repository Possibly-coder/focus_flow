from celery import shared_task
from django.utils import timezone
from .models import Todo

@shared_task
def notify_due_tasks():
    current_time = timezone.now()
    tasks = Todo.objects.filter(isCompleted=False)
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n \n \n \n \n ")
    for task in tasks:
        # Send notification to the user - could be email, app notification, etc.
        print(f"Reminder: It's time to complete your task: {task.title}")

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PIVO_API.settings')

app = Celery('PIVO_CELERY')

app.config_from_object('django.conf:settings', namespace='PIVO_API')
app.autodiscover_tasks()

app.conf.tasks = ['main_task']

app.conf.beat_schedule = {
    'run-task-every-minute': {
        'task': 'tasks.main_task',
        'schedule': crontab(minute='*/1'), 
    },
}
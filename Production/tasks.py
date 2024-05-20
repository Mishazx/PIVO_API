from celery import shared_task
from django.utils import timezone
import math
import random
from .models import ProductionLine, ProductionLinePerformance
from PIVO_API.celery import app

@app.task(name='tasks.main_task')
def main_task():
    print('task... started')
    production_lines = ProductionLine.objects.all()
    for production_line in production_lines:
        performance = math.ceil(30 + (100 - 30) * (random.random() ** 0.5))
        timestamp = timezone.now()
        ProductionLinePerformance.objects.create(
            production_line=production_line,
            timestamp=timestamp,
            performance=performance
        )
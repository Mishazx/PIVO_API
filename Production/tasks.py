from celery import shared_task
from django.utils import timezone
import math
import random
from .models import CharacteristicProductionLine, ProductionLine, ProductionLinePerformance
from PIVO_API.celery import app

MAINTENANCE_FREQUENCIES = ["Ежедневно", "Еженедельно", "Ежемесячно", "Ежеквартально", "Каждые полгода", "Ежегодно"]


def generation_performance(production_line):
    performance = math.ceil(30 + (100 - 30) * (random.random() ** 0.1))
    timestamp = timezone.now()
    ProductionLinePerformance.objects.create(
        production_line=production_line,
        timestamp=timestamp,
        performance=performance
    )
    
def generation_characteristic(production_line):
    operational_hours = random.randint(8, 24)  # Случайные операционные часы между 8 и 24
    maintenance_frequency = random.choice(MAINTENANCE_FREQUENCIES)  # Случайная частота технического обслуживания
    energy_consumption = round(random.uniform(500.0, 2000.0), 2)  # Случайное потребление энергии между 500 и 2000 кВт·ч
    staff_required = random.randint(5, 20)  # Случайное количество сотрудников между 5 и 20
    downtime_per_month = round(random.uniform(0.5, 10.0), 1)  # Случайное время простоя между 0.5 и 10 часов в месяц
    
    # Создание экземпляра CharacteristicProductionLine
    CharacteristicProductionLine.objects.create(
        production_line=production_line,
        operational_hours=operational_hours,
        maintenance_frequency=maintenance_frequency,
        energy_consumption=energy_consumption,
        staff_required=staff_required,
        downtime_per_month=downtime_per_month
    )
        
        # Сохранение экземпляра в базе данных
    # characteristic.save()

@app.task(name='tasks.main_task')
def main_task():
    print('task... started')
    production_lines = ProductionLine.objects.all()
    for production_line in production_lines:
        generation_performance(production_line)
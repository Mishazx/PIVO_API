from django.db import models

from Production.models import ProductionLine

# Create your models here.
class BrewingEvent(models.Model):
    id = models.AutoField(primary_key=True)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, verbose_name='Производственная линия')
    event_type = models.CharField(max_length=50, verbose_name='Тип события')
    event_date = models.DateField(verbose_name='Дата события')
    description = models.TextField(verbose_name='Описание события')
    
    def __str__(self):
        return f'{self.event_type} on {self.event_date}'
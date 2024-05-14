from django.db import models


class ProductionLine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название производственной линии')
    description = models.TextField(verbose_name='Описание производственной линии')
    def __str__(self):
        return self.name
    
class BrewingEvent(models.Model):
    id = models.AutoField(primary_key=True)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, verbose_name='Производственная линия')
    event_type = models.CharField(max_length=50, verbose_name='Тип события')
    event_date = models.DateField(verbose_name='Дата события')
    description = models.TextField(verbose_name='Описание события')
    
    def __str__(self):
        return f'{self.event_type} on {self.event_date}'
    
    
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, verbose_name='Производственная линия')
    def __str__(self):
        return self.name
    
# class Equipment(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, verbose_name='Название')
#     description = models.TextField(blank=True, verbose_name='Описание')
#     location = models.CharField(max_length=255, verbose_name='Местоположение')

#     def __str__(self):
#         return self.name
    
    
class TechnicalService(models.Model):
    id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')
    service_date = models.DateField(verbose_name='Дата технического обслуживания')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.equipment} --- {self.service_date}'
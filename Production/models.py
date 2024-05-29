from django.db import models


class ProductionLine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название производственной линии')
    description = models.TextField(verbose_name='Описание производственной линии')
    def __str__(self):
        return self.name
    
    

    
    
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, verbose_name='Производственная линия')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name
    
    
class TechnicalService(models.Model):
    id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, verbose_name='Производственная линия', default=None)
    service_date = models.DateField(verbose_name='Дата технического обслуживания')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.equipment}'
    
    
class ProductionLinePerformance(models.Model):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, help_text='Производительность производственной линии')
    timestamp = models.DateTimeField()
    performance = models.DecimalField(max_digits=10, decimal_places=3, help_text="Производительность в гектолитрах в час")
    
    
class CharacteristicProductionLine(models.Model):
    id = models.AutoField(primary_key=True)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, verbose_name='Производственная линия')
    status = models.CharField(max_length=100, help_text="Статус линии", default='')
    efficiency = models.FloatField(help_text="Эффективность производственной линии", default=0.0)
    operational_hours = models.IntegerField(help_text="Операционные часы в день")
    maintenance_frequency = models.CharField(max_length=100, help_text="Частота технического обслуживания")
    energy_consumption = models.FloatField(help_text="Потребление энергии в кВт·ч")
    staff_required = models.IntegerField(help_text="Количество сотрудников, необходимых для работы линии")
    downtime_per_month = models.FloatField(help_text="Время простоя в часах в месяц")
    last_updated = models.DateTimeField(auto_now=True)
    
    
class StorageData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    count = models.IntegerField(verbose_name='Количество')
    
    
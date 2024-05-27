from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    production_line = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
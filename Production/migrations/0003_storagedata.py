# Generated by Django 5.0.6 on 2024-05-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0002_productionlineperformance'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('count', models.IntegerField(verbose_name='Количество')),
            ],
        ),
    ]

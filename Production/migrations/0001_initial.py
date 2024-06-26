# Generated by Django 5.0.6 on 2024-05-15 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название производственной линии')),
                ('description', models.TextField(verbose_name='Описание производственной линии')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('production_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Production.productionline', verbose_name='Производственная линия')),
            ],
        ),
        migrations.CreateModel(
            name='BrewingEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type', models.CharField(max_length=50, verbose_name='Тип события')),
                ('event_date', models.DateField(verbose_name='Дата события')),
                ('description', models.TextField(verbose_name='Описание события')),
                ('production_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Production.productionline', verbose_name='Производственная линия')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_date', models.DateField(verbose_name='Дата технического обслуживания')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Production.equipment', verbose_name='Оборудование')),
            ],
        ),
    ]

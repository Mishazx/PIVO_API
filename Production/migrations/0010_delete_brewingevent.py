# Generated by Django 5.0.6 on 2024-05-29 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0009_technicalservice_production_line'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BrewingEvent',
        ),
    ]
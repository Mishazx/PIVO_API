# Generated by Django 5.0.6 on 2024-05-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos')),
                ('production_line', models.CharField(max_length=100)),
            ],
        ),
    ]

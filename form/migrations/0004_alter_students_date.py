# Generated by Django 4.2.3 on 2023-10-05 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_students_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

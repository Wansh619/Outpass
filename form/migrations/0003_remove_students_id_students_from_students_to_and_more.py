# Generated by Django 4.2.3 on 2023-09-10 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_students_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AddField(
            model_name='students',
            name='From',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='students',
            name='To',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='students',
            name='roll_no',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]

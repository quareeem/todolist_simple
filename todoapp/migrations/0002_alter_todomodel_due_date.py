# Generated by Django 4.1.2 on 2022-12-11 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 9, 17, 43, 142217, tzinfo=datetime.timezone.utc)),
        ),
    ]
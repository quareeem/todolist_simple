# Generated by Django 4.1.2 on 2022-12-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_todomodel_is_overdue_alter_todomodel_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='due_date',
            field=models.DateTimeField(default='2022.12.20-09:26:11'),
        ),
    ]

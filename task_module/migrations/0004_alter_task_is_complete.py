# Generated by Django 5.1.3 on 2024-12-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_module', '0003_rename_is_completed_task_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]

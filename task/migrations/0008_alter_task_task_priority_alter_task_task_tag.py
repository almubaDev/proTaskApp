# Generated by Django 5.0.2 on 2024-02-17 03:59

import django.db.models.deletion
import user_manager.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_task_task_priority_alter_task_task_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_priority',
            field=models.ForeignKey(limit_choices_to={'owner_priority': user_manager.models.CustomUser}, on_delete=django.db.models.deletion.CASCADE, to='task.priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_tag',
            field=models.ForeignKey(limit_choices_to={'owner_tag': user_manager.models.CustomUser}, on_delete=django.db.models.deletion.CASCADE, to='task.tag'),
        ),
    ]

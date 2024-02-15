# Generated by Django 5.0.2 on 2024-02-12 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_task_priority_alter_task_task_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='task.priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='task.tag'),
        ),
    ]

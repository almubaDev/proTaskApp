# Generated by Django 5.0.2 on 2024-02-21 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_alter_task_task_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_tag',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='task.tag'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-17 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_task_priority_alter_task_task_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_owner',
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_tag_background_color_alter_task_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=models.CharField(default='#59B4C3', max_length=7),
        ),
    ]

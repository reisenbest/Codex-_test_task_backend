# Generated by Django 4.2.6 on 2023-10-06 22:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0006_metric_delete_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='metric',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-06 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_note_remove_metric_event_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('genre', models.CharField(choices=[('poetry', 'Стих'), ('story', 'Рассказ'), ('fairytale', 'Сказка'), ('other', 'Другое')], default='other', max_length=20)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Metric',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]

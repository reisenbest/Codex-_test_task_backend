from django.utils import timezone
from .models import Metric

def add_hardcoded_metrics():
    # Проверка наличия данных чтобы не добавлять с каждым запуском новые
    if not Metric.objects.filter(name="note_view").exists():
        # Хардкодированные данные
        metrics_data = [
            {"name": "note_view", "value": 1, "event_id": 1},
            {"name": "note_view", "value": 1, "event_id": 1},
            {"name": "note_reading_time", "value": 5, "event_id": 1},
            {"name": "note_reading_time", "value": 7, "event_id": 1},
            {"name": "navigation_button_click", "value": 1, "event_id": 1},
            {"name": "navigation_button_click", "value": 1, "event_id": 1},
            {"name": "time_to_edit_note", "value": 10, "event_id": 1},
            {"name": "time_to_edit_note", "value": 15, "event_id": 1},
        ]

        # Сохранение данных в базу данных
        for data in metrics_data:
            Metric.objects.create(
                name=data['name'],
                value=data.get('value', 0.0),
                create_time=timezone.now(),
                update_time=timezone.now(),
                event_id=data.get('event_id', None)
            )
        print("Хардкодированные данные  добавлены.")
    else:
        print("Хардкодированные данные уже существуют.")



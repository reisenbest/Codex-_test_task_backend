
from django.db import models
from django.utils import timezone

class Metric(models.Model):
    name = models.CharField(max_length=255) #имя метрики (например общее количество записок)
    value = models.FloatField() #само количиество
    create_time = models.DateTimeField( default=timezone.now)
    update_time = models.DateTimeField (default=timezone.now)
    event_id = models.IntegerField(null=True) #чтобы различать источники, например данные из разных итсточников имеют разные id

    def __str__(self):
        return f'{self.name} - {self.value} ({self.create_time})'

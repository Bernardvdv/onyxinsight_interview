from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    name = models.CharField(max_length=180, unique=True)
    unit = models.CharField(max_length=180)


class Data(models.Model):
    date = models.DateTimeField(default=timezone.now)
    sensor = models.CharField(max_length=180)
    value = models.FloatField()

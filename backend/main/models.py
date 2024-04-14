from django.db import models

# Create your models here.
class Device(models.Model):
  name = models.CharField(max_length=50)

class HistoricPower(models.Model):
  date = models.DateTimeField()
  power = models.DecimalField()

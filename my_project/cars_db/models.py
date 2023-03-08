from django.db import models

class Car(models.Model):
  year = models.IntegerField()
  make = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  color = models.CharField(max_length=255)
  died = models.CharField(max_length=255)
from django.db import models

class Car(models.Model):
  year = models.IntegerField()
  make = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  color = models.CharField(max_length=255)
  died = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.year} {self.make} {self.model}"
  
# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   email = models.CharField(max_length=255)

#   def __str__(self):
#     return f"{self.firstname} {self.lastname}"
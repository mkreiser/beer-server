from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here. # Don't tell me what to do.

class Beer(models.Model):
  ranking = models.IntegerField()
  brewery = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  comments = models.TextField(blank=True)
  # tags = ArrayField(models.CharField(max_length=50)) # Im being lazy

  def __str__(self):
    return self.brewery + ' ' + self.name

from django.db import models

# Create your models here.

class List(models.Model):
  objects = models.Manager()
  pass
  
class Item(models.Model):
  text = models.TextField(default='')
  objects = models.Manager()
  list = models.ForeignKey(List, default=None)


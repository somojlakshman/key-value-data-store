from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=22,blank=True)
    des=models.TextField(blank=True)

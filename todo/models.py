from django.db import models

# Create your models here.
class Todo(models.Model):
    label = models.CharField(max_length=100)
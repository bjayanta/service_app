from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = (
        ('Done', 'Done'),
        ('Pending', 'Pending'),
        ('Running', 'Running')
    )

    label = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    reminder = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

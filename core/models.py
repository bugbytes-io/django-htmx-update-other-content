from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
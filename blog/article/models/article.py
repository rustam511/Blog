from django.db import models
from django.contrib.auth import User
from datetime import datetime

class Article(models.Model):
    user = models.Foreignkey(User, default=1)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=100000)
    dt = models.DateTimeField(
        default=datetime.now(),
          blank=True)

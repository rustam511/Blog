
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=100000)
    dt = models.DateTimeField(default=datetime.now(), blank=True)
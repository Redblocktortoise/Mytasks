from datetime import timezone
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    author = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
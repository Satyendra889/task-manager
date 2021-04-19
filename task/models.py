from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')


class Entry(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
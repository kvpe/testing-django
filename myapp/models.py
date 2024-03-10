from django.db import models
from django.contrib.auth.models import User

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField()

class Discussion(models.Model):
    poi = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

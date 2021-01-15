from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=100)
    year = models.IntegerField(())
    mood = models.CharField(max_length=50)
    notes = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

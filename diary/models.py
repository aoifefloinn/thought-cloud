from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings

# Create your models here.
class Entry(models.Model):
    class Mood(models.IntegerChoices):
        HAPPY=1
        SMILING=2
        LAUGHING=3
        LOVLY=4
        GRUMPY=5
        SAD=6
        WORRIED=7
        EYESROLL=8
        SLEEPY=9
        CRYING=10
        OFFENDED=11
        AMAZED=12
        SHOCKED=13
        SCARED=14
        HYPNOTIZED=15
        ANGRY=16
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="diary_user", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default = datetime.now)
    content = models.TextField()
    location = models.CharField(max_length=100, null=True, blank=True)
    mood = models.IntegerField(choices=Mood.choices)


class DiaryImages(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)


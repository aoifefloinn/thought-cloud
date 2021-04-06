from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Color(models.IntegerChoices):
        feb67b=1
        fe7b82=2
        e6b8e9=3
        abb287=4
        bcdca0=5
        e6ccff=6
        f04020=7
        e0e040=8
        a0dcc0=9

    profile_img = models.ImageField(upload_to='profile', blank=True, null=True, default='user\image\default.png')
    theme = models.IntegerField(choices=Color.choices, blank=True, null=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Color(models.Model):
        feb67b=1
        fe7b82=2
        e6b8e9=3
        abb287=4
    profile_img = models.ImageField(upload_to='profile', blank=True, null=True, default='user\image\default.png')
    theme = models.IntegerField(choices=Color.choices)

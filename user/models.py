from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    profile_img = models.ImageField(upload_to='profile', blank=True, null=True, default='user\image\default.png')
    theme = models.IntegerField(choices=Color.choices, blank=True, null=True, default=1)

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.Profile.save()


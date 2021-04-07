from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    class Colors(models.IntegerChoices):
        feb67b=1
        fe7b82=2
        e6b8e9=3
        abb287=4
        bcdca0=5
        e6ccff=6
        f04020=7
        e0e040=8
        a0dcc0=9
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Profile')
    profile_img = models.ImageField(upload_to='profile', blank=True, null=True, default='user\image\default.png')
    theme = models.IntegerField(choices=Colors.choices, blank=True, null=True, default=1)

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.Profile.save()

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
 
 
class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            email=MyUserManager.normalize_email(email),
            nickname=nickname,            
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, nickname, password):
        u = self.create_user(email=email,
                             nickname=nickname,
                             password=password,
                             )
        u.is_admin = True
        u.save(using=self._db)
        return u
 
 
class MyUser(AbstractBaseUser,  PermissionsMixin):
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
    
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        'nickname', 
        max_length=10, 
        blank=False, 
        unique=True, 
        default='')
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatar',
    )
    theme = models.IntegerField(
        choices=Color.choices, 
        blank=True, 
        null=True, 
        default=1
    )

 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
 
    objects = MyUserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']
 
    def get_full_name(self):
        # The user is identified by their email address
        return self.email
 
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
 
    def __str__(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.images import get_image_dimensions
from .models import MyUser

# class SignUpForm(UserCreationForm):
    # pass
    # profile_img = forms.ImageField()
    # theme = forms.IntegerField()
    # class Meta:
    #     model=MyUser
    #     fields=('profile_img', 'email', 'password','username', 'theme',)

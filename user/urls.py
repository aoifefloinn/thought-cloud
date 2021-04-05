from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/", include('allauth.urls')),
    path('', views.index, name='home'),
]
